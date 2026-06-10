const API_BASE_URL = "http://127.0.0.1:5000";

const form = document.getElementById("mentorForm");
const atsButton = document.getElementById("atsButton");
const outputScreen = document.getElementById("outputScreen");

function escapeHtml(text) {

    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
}

function showLoading(message = "Processing Request...") {

    outputScreen.innerHTML = `
        <div class="card">

            <div class="card-title">
                ${message}
            </div>

            <p>
                Please wait...
            </p>

        </div>
    `;
}

function showError(message) {

    outputScreen.innerHTML = `
        <div class="card">

            <div class="card-title">
                Error
            </div>

            <p>
                ${escapeHtml(message)}
            </p>

        </div>
    `;
}

function renderAnalysis(data) {

    outputScreen.innerHTML = `
        <div class="card">

            <div class="card-title">
                AI Career Analysis
            </div>

            <div style="white-space: pre-wrap; line-height: 1.8;">
                ${escapeHtml(data.analysis)}
            </div>

        </div>
    `;
}

function renderATS(data) {

    const skills = data.detected_skills
        .map(skill => `
            <span class="badge">
                ${escapeHtml(skill)}
            </span>
        `)
        .join("");

    const missing = data.missing_keywords
        .map(skill => `
            <span class="badge">
                ${escapeHtml(skill)}
            </span>
        `)
        .join("");

    const feedback = data.feedback
        .map(item => `
            <li>${escapeHtml(item)}</li>
        `)
        .join("");

    outputScreen.innerHTML = `
        <div class="card">

            <div class="card-title">
                ATS Analysis
            </div>

            <p>
                <strong>ATS Score:</strong>
                ${data.ats_score}/100
            </p>

            <br>

            <strong>
                Detected Skills
            </strong>

            <br><br>

            ${skills || "None"}

            <br><br>

            <strong>
                Missing Keywords
            </strong>

            <br><br>

            ${missing || "None"}

            <br><br>

            <strong>
                Suggestions
            </strong>

            <ul>
                ${feedback}
            </ul>

        </div>
    `;
}

async function getCareerAnalysis(
    skills,
    project,
    target
) {

    const response = await fetch(
        `${API_BASE_URL}/api/analyze`,
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                skills,
                project_description: project,
                target_focus: target
            })
        }
    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(
            data.error ||
            "Analysis failed."
        );
    }

    return data;
}

async function getATSAnalysis(
    resumeText,
    targetRole
) {

    const response = await fetch(
        `${API_BASE_URL}/api/ats`,
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                resume_text: resumeText,
                target_role: targetRole
            })
        }
    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(
            data.error ||
            "ATS analysis failed."
        );
    }

    return data;
}

form.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();

        const skills = document
            .getElementById("skills")
            .value
            .trim();

        const project = document
            .getElementById("project")
            .value
            .trim();

        const target = document
            .getElementById("target")
            .value
            .trim();

        try {

            showLoading(
                "Generating Career Analysis..."
            );

            const analysis =
                await getCareerAnalysis(
                    skills,
                    project,
                    target
                );

            renderAnalysis(
                analysis
            );

        } catch(error) {

            showError(
                error.message
            );
        }
    }
);

atsButton.addEventListener(
    "click",
    async function() {

        const skills = document
            .getElementById("skills")
            .value
            .trim();

        const project = document
            .getElementById("project")
            .value
            .trim();

        const target = document
            .getElementById("target")
            .value
            .trim();

        const resumeText = `
Skills:
${skills}

Projects:
${project}
        `;

        try {

            showLoading(
                "Running ATS Analysis..."
            );

            const result =
                await getATSAnalysis(
                    resumeText,
                    target
                );

            renderATS(
                result
            );

        } catch(error) {

            showError(
                error.message
            );
        }
    }
);
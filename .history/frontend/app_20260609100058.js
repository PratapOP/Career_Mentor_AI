const API_BASE_URL = "http://127.0.0.1:5000";

const form = document.getElementById(
    "mentorForm"
);

const outputScreen = document.getElementById(
    "outputScreen"
);

function showLoading() {

    outputScreen.innerHTML = `
        <div class="card">
            <div class="card-title">
                Processing Request...
            </div>

            <p>
                Analyzing profile and generating recommendations.
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

            <p>${message}</p>
        </div>
    `;
}

function createBadge(skill) {

    return `
        <span class="badge">
            ${skill}
        </span>
    `;
}

function renderAnalysis(data) {

    outputScreen.innerHTML = `
        <div class="card">

            <div class="card-title">
                AI Career Analysis
            </div>

            <pre>${data.analysis}</pre>

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
                skills: skills,
                project_description: project,
                target_focus: target
            })
        }
    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(
            data.error ||
            "Career analysis failed."
        );
    }

    return data;
}

form.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();

        const skills =
            document
                .getElementById("skills")
                .value
                .trim();

        const project =
            document
                .getElementById("project")
                .value
                .trim();

        const target =
            document
                .getElementById("target")
                .value
                .trim();

        try {

            showLoading();

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
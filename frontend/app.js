document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("mentorForm");
    const outputScreen = document.getElementById("outputScreen");

    form.addEventListener("submit", async (event) => {

        event.preventDefault();

        const skills = document.getElementById("skills").value.trim();
        const project = document.getElementById("project").value.trim();
        const target = document.getElementById("target").value.trim();

        outputScreen.innerHTML = `
            <div class="terminal-prompt">
                Running career analysis...
            </div>
        `;

        try {

            const response = await fetch(
                "http://127.0.0.1:5000/api/analyze",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
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
                    data.error || "Unknown server error"
                );
            }

            outputScreen.innerHTML = `
                <pre style="white-space: pre-wrap; word-wrap: break-word;">
${data.analysis}
                </pre>
            `;

        } catch (error) {

            outputScreen.innerHTML = `
                <div style="color:#ff5c5c;">
                    ERROR: ${error.message}
                </div>
            `;
        }

    });

});
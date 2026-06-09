from flask import Flask, request, jsonify
from flask_cors import CORS

from backend.services.inference_service import CareerMentor

app = Flask(__name__)
CORS(app)

mentor = CareerMentor()


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/analyze", methods=["POST"])
def analyze():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No JSON payload received."
            }), 400

        skills = data.get("skills", "").strip()
        project_description = data.get(
            "project_description",
            ""
        ).strip()
        target_focus = data.get(
            "target_focus",
            ""
        ).strip()

        if not skills:
            return jsonify({
                "error": "Skills field is required."
            }), 400

        if not project_description:
            return jsonify({
                "error": "Project description field is required."
            }), 400

        if not target_focus:
            return jsonify({
                "error": "Target role field is required."
            }), 400

        analysis = mentor.generate(
            skills=skills,
            project_description=project_description,
            target_focus=target_focus
        )

        return jsonify({
            "analysis": analysis
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
from flask import (
    Flask,
    jsonify,
    request
)

from flask_cors import CORS

from services.inference_service import CareerMentor
from services.resume_parser import ResumeParser
from services.ats_service import ATSService
from services.roadmap_service import RoadmapService
from services.recommendation_service import RecommendationService
from services.interview_service import InterviewService
from services.skill_gap_service import SkillGapService


app = Flask(__name__)

CORS(app)

mentor = CareerMentor()
resume_parser = ResumeParser()
ats_service = ATSService()
roadmap_service = RoadmapService()
recommendation_service = RecommendationService()
interview_service = InterviewService()
skill_gap_service = SkillGapService()


@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "healthy"
    })


@app.route("/api/analyze", methods=["POST"])
def analyze():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "success": False,
                "error": "No input provided."
            }), 400

        skills = data.get(
            "skills",
            ""
        ).strip()

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
                "success": False,
                "error": "Skills are required."
            }), 400

        if not project_description:

            return jsonify({
                "success": False,
                "error": "Project description is required."
            }), 400

        if not target_focus:

            return jsonify({
                "success": False,
                "error": "Target role is required."
            }), 400

        analysis = mentor.generate(
            skills=skills,
            project_description=project_description,
            target_focus=target_focus
        )

        return jsonify({
            "success": True,
            "analysis": analysis
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/api/ats", methods=["POST"])
def ats_score():

    try:

        data = request.get_json()

        resume_text = data.get(
            "resume_text",
            ""
        )

        target_role = data.get(
            "target_role",
            ""
        )

        result = ats_service.calculate_score(
            resume_text=resume_text,
            target_role=target_role
        )

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/roadmap", methods=["POST"])
def roadmap():

    try:

        data = request.get_json()

        current_skills = data.get(
            "skills",
            []
        )

        target_role = data.get(
            "target_role",
            ""
        )

        result = roadmap_service.generate(
            current_skills=current_skills,
            target_role=target_role
        )

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/recommendations", methods=["POST"])
def recommendations():

    try:

        data = request.get_json()

        skills = data.get(
            "skills",
            []
        )

        target_role = data.get(
            "target_role",
            ""
        )

        result = recommendation_service.recommend(
            skills=skills,
            target_role=target_role
        )

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/interview", methods=["POST"])
def interview():

    try:

        data = request.get_json()

        target_role = data.get(
            "target_role",
            ""
        )

        experience_level = data.get(
            "experience_level",
            "beginner"
        )

        result = interview_service.generate_questions(
            target_role=target_role,
            experience_level=experience_level
        )

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/skill-gap", methods=["POST"])
def skill_gap():

    try:

        data = request.get_json()

        skills = data.get(
            "skills",
            []
        )

        target_role = data.get(
            "target_role",
            ""
        )

        if isinstance(skills, str):

            skills = [
                skill.strip()
                for skill in skills.split(",")
                if skill.strip()
            ]

        result = skill_gap_service.analyze(
            current_skills=skills,
            target_role=target_role
        )

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/parse-resume", methods=["POST"])
def parse_resume():

    try:

        data = request.get_json()

        file_path = data.get(
            "file_path",
            ""
        )

        result = resume_parser.parse_resume(
            file_path
        )

        return jsonify(result)

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
class JobMatchService:

    def match(
        self,
        resume_text,
        target_role
    ):

        role = target_role.lower()

        role_requirements = {

            "data scientist": [
                "python",
                "sql",
                "pandas",
                "numpy",
                "machine learning",
                "statistics"
            ],

            "machine learning engineer": [
                "python",
                "pytorch",
                "tensorflow",
                "docker",
                "machine learning"
            ],

            "backend developer": [
                "python",
                "flask",
                "fastapi",
                "sql",
                "api"
            ],

            "full stack developer": [
                "html",
                "css",
                "javascript",
                "react",
                "node"
            ]
        }

        requirements = role_requirements.get(
            role,
            []
        )

        resume_lower = resume_text.lower()

        matched_skills = []
        missing_skills = []

        for skill in requirements:

            if skill in resume_lower:
                matched_skills.append(
                    skill
                )
            else:
                missing_skills.append(
                    skill
                )

        if requirements:

            match_percentage = int(
                (
                    len(matched_skills)
                    /
                    len(requirements)
                ) * 100
            )

        else:

            match_percentage = 0

        return {
            "target_role": target_role,
            "match_percentage": match_percentage,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }
class SkillGapService:

    def analyze(
        self,
        current_skills,
        target_role
    ):

        role = target_role.lower()

        role_requirements = {

            "data scientist": [
                "Python",
                "SQL",
                "Pandas",
                "NumPy",
                "Statistics",
                "Machine Learning",
                "Data Visualization"
            ],

            "machine learning engineer": [
                "Python",
                "PyTorch",
                "TensorFlow",
                "Docker",
                "MLOps",
                "Machine Learning",
                "Deep Learning"
            ],

            "backend developer": [
                "Python",
                "Flask",
                "FastAPI",
                "SQL",
                "Docker",
                "REST APIs",
                "System Design"
            ],

            "full stack developer": [
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Node.js",
                "MongoDB",
                "REST APIs"
            ],

            "devops engineer": [
                "Linux",
                "Docker",
                "Kubernetes",
                "AWS",
                "CI/CD",
                "Terraform",
                "Monitoring"
            ]
        }

        required_skills = role_requirements.get(
            role,
            []
        )

        current_skills_set = {
            skill.strip().lower()
            for skill in current_skills
        }

        matched_skills = []
        missing_skills = []

        for skill in required_skills:

            if skill.lower() in current_skills_set:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        completion_percentage = 0

        if required_skills:

            completion_percentage = int(
                (
                    len(matched_skills)
                    /
                    len(required_skills)
                ) * 100
            )

        learning_priority = []

        for skill in missing_skills:

            learning_priority.append({
                "skill": skill,
                "priority": "High"
            })

        return {
            "target_role": target_role,
            "completion_percentage": completion_percentage,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "learning_priority": learning_priority
        }
class RoadmapService:

    def generate(
        self,
        current_skills,
        target_role
    ):

        role = target_role.lower()

        roadmaps = {

            "data scientist": {
                "month_1": [
                    "Python",
                    "NumPy",
                    "Pandas"
                ],
                "month_2": [
                    "Statistics",
                    "Data Cleaning",
                    "EDA"
                ],
                "month_3": [
                    "Machine Learning",
                    "Scikit-Learn"
                ],
                "month_4": [
                    "Projects",
                    "Model Deployment"
                ]
            },

            "machine learning engineer": {
                "month_1": [
                    "Python",
                    "NumPy",
                    "Pandas"
                ],
                "month_2": [
                    "Machine Learning",
                    "Scikit-Learn"
                ],
                "month_3": [
                    "PyTorch",
                    "TensorFlow"
                ],
                "month_4": [
                    "MLOps",
                    "Docker",
                    "Deployment"
                ]
            },

            "backend developer": {
                "month_1": [
                    "Python",
                    "OOP",
                    "SQL"
                ],
                "month_2": [
                    "Flask",
                    "REST APIs"
                ],
                "month_3": [
                    "Authentication",
                    "Caching"
                ],
                "month_4": [
                    "Docker",
                    "Deployment"
                ]
            },

            "full stack developer": {
                "month_1": [
                    "HTML",
                    "CSS",
                    "JavaScript"
                ],
                "month_2": [
                    "React"
                ],
                "month_3": [
                    "Node.js",
                    "APIs"
                ],
                "month_4": [
                    "Deployment",
                    "Docker"
                ]
            }
        }

        roadmap = roadmaps.get(
            role,
            {
                "month_1": [
                    "Programming Fundamentals"
                ],
                "month_2": [
                    "Projects"
                ],
                "month_3": [
                    "Advanced Topics"
                ],
                "month_4": [
                    "Portfolio Building"
                ]
            }
        )

        return {
            "target_role": target_role,
            "current_skills": current_skills,
            "roadmap": roadmap
        }
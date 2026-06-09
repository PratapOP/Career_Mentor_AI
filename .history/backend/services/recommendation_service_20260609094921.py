class RecommendationService:

    def recommend(
        self,
        skills,
        target_role
    ):

        role = target_role.lower()

        recommendations = {

            "data scientist": {
                "projects": [
                    "Customer Churn Prediction",
                    "House Price Prediction",
                    "Sales Forecasting"
                ],
                "courses": [
                    "Machine Learning Specialization",
                    "Data Analysis with Python",
                    "Statistics for Data Science"
                ],
                "tools": [
                    "Pandas",
                    "NumPy",
                    "Scikit-Learn",
                    "Matplotlib"
                ]
            },

            "machine learning engineer": {
                "projects": [
                    "Image Classification System",
                    "Sentiment Analysis Pipeline",
                    "Recommendation Engine"
                ],
                "courses": [
                    "Deep Learning Specialization",
                    "PyTorch Fundamentals",
                    "MLOps Fundamentals"
                ],
                "tools": [
                    "PyTorch",
                    "TensorFlow",
                    "Docker",
                    "MLflow"
                ]
            },

            "backend developer": {
                "projects": [
                    "Authentication API",
                    "Booking System",
                    "Payment Gateway Service"
                ],
                "courses": [
                    "REST API Design",
                    "Database Design",
                    "System Design Basics"
                ],
                "tools": [
                    "Flask",
                    "FastAPI",
                    "PostgreSQL",
                    "Docker"
                ]
            },

            "full stack developer": {
                "projects": [
                    "E-Commerce Platform",
                    "Social Media App",
                    "Task Management System"
                ],
                "courses": [
                    "React Mastery",
                    "Node.js Development",
                    "Full Stack Web Development"
                ],
                "tools": [
                    "React",
                    "Node.js",
                    "MongoDB",
                    "Docker"
                ]
            }
        }

        result = recommendations.get(
            role,
            {
                "projects": [
                    "Portfolio Website",
                    "Automation Tool",
                    "Problem Solving Project"
                ],
                "courses": [
                    "Programming Fundamentals"
                ],
                "tools": [
                    "Git",
                    "GitHub"
                ]
            }
        )

        return {
            "target_role": target_role,
            "current_skills": skills,
            "recommended_projects": result["projects"],
            "recommended_courses": result["courses"],
            "recommended_tools": result["tools"]
        }
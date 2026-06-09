class ProjectGeneratorService:

    def generate(
        self,
        target_role
    ):

        role = target_role.lower()

        projects = {

            "data scientist": [
                {
                    "title": "Customer Churn Prediction",
                    "difficulty": "Intermediate",
                    "skills": [
                        "Python",
                        "Pandas",
                        "Scikit-Learn"
                    ]
                },
                {
                    "title": "House Price Prediction",
                    "difficulty": "Beginner",
                    "skills": [
                        "Regression",
                        "EDA",
                        "Data Visualization"
                    ]
                },
                {
                    "title": "Sales Forecasting Dashboard",
                    "difficulty": "Advanced",
                    "skills": [
                        "Time Series",
                        "Machine Learning",
                        "Deployment"
                    ]
                }
            ],

            "machine learning engineer": [
                {
                    "title": "Image Classification System",
                    "difficulty": "Intermediate",
                    "skills": [
                        "PyTorch",
                        "CNN",
                        "Computer Vision"
                    ]
                },
                {
                    "title": "Sentiment Analysis Engine",
                    "difficulty": "Intermediate",
                    "skills": [
                        "NLP",
                        "Transformers",
                        "Hugging Face"
                    ]
                },
                {
                    "title": "MLOps Pipeline",
                    "difficulty": "Advanced",
                    "skills": [
                        "Docker",
                        "CI/CD",
                        "Model Deployment"
                    ]
                }
            ],

            "backend developer": [
                {
                    "title": "Booking Management API",
                    "difficulty": "Intermediate",
                    "skills": [
                        "Flask",
                        "PostgreSQL",
                        "REST APIs"
                    ]
                },
                {
                    "title": "Authentication Service",
                    "difficulty": "Intermediate",
                    "skills": [
                        "JWT",
                        "Security",
                        "Databases"
                    ]
                },
                {
                    "title": "Microservice Architecture",
                    "difficulty": "Advanced",
                    "skills": [
                        "Docker",
                        "Redis",
                        "Scalability"
                    ]
                }
            ],

            "full stack developer": [
                {
                    "title": "E-Commerce Platform",
                    "difficulty": "Advanced",
                    "skills": [
                        "React",
                        "Flask",
                        "Payments"
                    ]
                },
                {
                    "title": "Task Management App",
                    "difficulty": "Intermediate",
                    "skills": [
                        "CRUD",
                        "Authentication",
                        "Deployment"
                    ]
                },
                {
                    "title": "Social Media Platform",
                    "difficulty": "Advanced",
                    "skills": [
                        "Realtime Systems",
                        "WebSockets",
                        "Databases"
                    ]
                }
            ]
        }

        return {
            "target_role": target_role,
            "projects": projects.get(
                role,
                [
                    {
                        "title": "Portfolio Website",
                        "difficulty": "Beginner",
                        "skills": [
                            "HTML",
                            "CSS",
                            "JavaScript"
                        ]
                    }
                ]
            )
        }
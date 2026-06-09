class CareerPathService:

    def generate(
        self,
        target_role
    ):

        role = target_role.lower()

        paths = {

            "data scientist": {
                "career_path": [
                    "Data Analyst",
                    "Junior Data Scientist",
                    "Data Scientist",
                    "Senior Data Scientist",
                    "Lead Data Scientist",
                    "Head of Data Science"
                ],
                "salary_range_usd": {
                    "entry": "60,000 - 90,000",
                    "mid": "90,000 - 140,000",
                    "senior": "140,000 - 220,000"
                }
            },

            "machine learning engineer": {
                "career_path": [
                    "ML Intern",
                    "Junior ML Engineer",
                    "ML Engineer",
                    "Senior ML Engineer",
                    "Staff ML Engineer",
                    "ML Architect"
                ],
                "salary_range_usd": {
                    "entry": "70,000 - 110,000",
                    "mid": "110,000 - 170,000",
                    "senior": "170,000 - 280,000"
                }
            },

            "backend developer": {
                "career_path": [
                    "Junior Backend Developer",
                    "Backend Developer",
                    "Senior Backend Developer",
                    "Lead Backend Engineer",
                    "Software Architect",
                    "Engineering Manager"
                ],
                "salary_range_usd": {
                    "entry": "60,000 - 100,000",
                    "mid": "100,000 - 150,000",
                    "senior": "150,000 - 250,000"
                }
            },

            "full stack developer": {
                "career_path": [
                    "Junior Full Stack Developer",
                    "Full Stack Developer",
                    "Senior Full Stack Developer",
                    "Lead Engineer",
                    "Software Architect",
                    "CTO"
                ],
                "salary_range_usd": {
                    "entry": "60,000 - 100,000",
                    "mid": "100,000 - 160,000",
                    "senior": "160,000 - 250,000"
                }
            }
        }

        default_path = {
            "career_path": [
                "Intern",
                "Junior Developer",
                "Developer",
                "Senior Developer",
                "Lead Developer"
            ],
            "salary_range_usd": {
                "entry": "40,000 - 70,000",
                "mid": "70,000 - 120,000",
                "senior": "120,000 - 200,000"
            }
        }

        result = paths.get(
            role,
            default_path
        )

        return {
            "target_role": target_role,
            "career_path": result["career_path"],
            "salary_range_usd": result["salary_range_usd"]
        }
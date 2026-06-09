import re


class ATSService:

    def calculate_score(
        self,
        resume_text,
        target_role=""
    ):

        score = 0

        feedback = []

        if len(resume_text) > 1000:
            score += 15
        else:
            feedback.append(
                "Resume content is too short."
            )

        if self._has_email(resume_text):
            score += 10
        else:
            feedback.append(
                "Email address missing."
            )

        if self._has_phone(resume_text):
            score += 10
        else:
            feedback.append(
                "Phone number missing."
            )

        sections = [
            "education",
            "skills",
            "projects",
            "experience"
        ]

        for section in sections:

            if section.lower() in resume_text.lower():
                score += 10
            else:
                feedback.append(
                    f"Missing section: {section}"
                )

        detected_skills = self.extract_skills(
            resume_text
        )

        score += min(
            len(detected_skills) * 2,
            25
        )

        if target_role:

            role_keywords = self.role_keywords(
                target_role
            )

            matched = len(
                set(role_keywords)
                &
                set(detected_skills)
            )

            score += min(
                matched * 2,
                20
            )

            missing_keywords = list(
                set(role_keywords)
                - set(detected_skills)
            )

        else:

            missing_keywords = []

        score = min(score, 100)

        return {
            "ats_score": score,
            "detected_skills": sorted(
                list(detected_skills)
            ),
            "missing_keywords": sorted(
                missing_keywords
            ),
            "feedback": feedback
        }

    def extract_skills(
        self,
        text
    ):

        skill_bank = {

            "python",
            "java",
            "c++",
            "c",
            "sql",
            "mysql",
            "postgresql",
            "mongodb",
            "html",
            "css",
            "javascript",
            "react",
            "nodejs",
            "flask",
            "django",
            "fastapi",
            "git",
            "github",
            "docker",
            "kubernetes",
            "aws",
            "azure",
            "tensorflow",
            "pytorch",
            "machine learning",
            "deep learning",
            "nlp",
            "pandas",
            "numpy",
            "scikit-learn"
        }

        text_lower = text.lower()

        found = set()

        for skill in skill_bank:

            if skill in text_lower:
                found.add(skill)

        return found

    def role_keywords(
        self,
        role
    ):

        role = role.lower()

        mapping = {

            "data scientist": [
                "python",
                "sql",
                "pandas",
                "numpy",
                "machine learning",
                "scikit-learn"
            ],

            "machine learning engineer": [
                "python",
                "tensorflow",
                "pytorch",
                "docker",
                "machine learning"
            ],

            "backend developer": [
                "python",
                "flask",
                "fastapi",
                "sql",
                "docker"
            ],

            "full stack developer": [
                "html",
                "css",
                "javascript",
                "react",
                "nodejs"
            ]
        }

        return mapping.get(
            role,
            []
        )

    def _has_email(
        self,
        text
    ):

        return bool(
            re.search(
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                text
            )
        )

    def _has_phone(
        self,
        text
    ):

        return bool(
            re.search(
                r"(\+?\d[\d\s\-\(\)]{8,}\d)",
                text
            )
        )
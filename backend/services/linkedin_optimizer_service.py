class LinkedInOptimizerService:

    def optimize(
        self,
        name,
        target_role,
        skills,
        experience_summary
    ):

        headline = (
            f"{target_role} | "
            f"{skills} | "
            f"Building Real-World Solutions"
        )

        about = f"""
I am an aspiring {target_role} with experience in {skills}.

My work includes {experience_summary}. I enjoy solving technical problems, building impactful applications, and continuously improving my skills through hands-on projects.

Currently focused on growing expertise in industry-relevant technologies while creating projects that demonstrate practical problem-solving and engineering abilities.

Open to internships, collaborations, and opportunities that help create meaningful impact through technology.
""".strip()

        keywords = [
            target_role,
            "Problem Solving",
            "Software Development",
            "Projects",
            "Leadership",
            "Teamwork",
            "Communication"
        ]

        recommendations = [
            "Use a professional profile photo.",
            "Add measurable project achievements.",
            "Include GitHub portfolio links.",
            "Add certifications and achievements.",
            "Request recommendations from mentors.",
            "Keep headline keyword-rich.",
            "Post project updates regularly."
        ]

        return {
            "name": name,
            "headline": headline,
            "about_section": about,
            "keywords": keywords,
            "recommendations": recommendations
        }
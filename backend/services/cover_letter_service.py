class CoverLetterService:

    def generate(
        self,
        name,
        target_role,
        company_name,
        skills,
        project_summary
    ):

        cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for the {target_role} position at {company_name}.

My background includes experience with {skills}. I have worked on projects such as {project_summary}, where I developed practical technical and problem-solving skills that directly align with the requirements of this role.

I am particularly interested in joining {company_name} because of its reputation for innovation and excellence. I am confident that my technical abilities, willingness to learn, and passion for building impactful solutions would allow me to contribute effectively to your team.

I would welcome the opportunity to discuss how my skills and experiences align with your organization's goals.

Thank you for your time and consideration.

Sincerely,

{name}
"""

        return {
            "candidate_name": name,
            "target_role": target_role,
            "company_name": company_name,
            "cover_letter": cover_letter.strip()
        }
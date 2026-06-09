import re
from pathlib import Path

import pdfplumber
from docx import Document


class ResumeParser:

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".docx",
        ".txt"
    }

    def extract_text(self, file_path):

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        extension = file_path.suffix.lower()

        if extension not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        if extension == ".pdf":
            return self._extract_pdf(file_path)

        if extension == ".docx":
            return self._extract_docx(file_path)

        if extension == ".txt":
            return self._extract_txt(file_path)

        return ""

    def _extract_pdf(self, file_path):

        text = []

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text.append(page_text)

        return "\n".join(text)

    def _extract_docx(self, file_path):

        document = Document(file_path)

        paragraphs = [
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        return "\n".join(paragraphs)

    def _extract_txt(self, file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            return file.read()

    def extract_email(self, text):

        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        return match.group(0) if match else None

    def extract_phone(self, text):

        match = re.search(
            r"(\+?\d[\d\s\-\(\)]{8,}\d)",
            text
        )

        return match.group(0) if match else None

    def extract_links(self, text):

        return re.findall(
            r"https?://[^\s]+",
            text
        )

    def parse_resume(self, file_path):

        text = self.extract_text(file_path)

        return {
            "raw_text": text,
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "links": self.extract_links(text)
        }
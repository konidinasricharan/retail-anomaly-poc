import pdfplumber
import re

def clean_text(text: str) -> str:
    if not text:
        return ""
    # Remove extra spaces and non-ASCII chars
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    return text.strip()

def parse_resume_pdf(pdf_path: str) -> str:
    extracted_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += " " + page_text

    return clean_text(extracted_text)

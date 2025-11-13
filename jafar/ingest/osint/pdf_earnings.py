import PyPDF2
import requests
from typing import str
import structlog

logger = structlog.get_logger()

def extract_earnings_text(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open("temp.pdf", "wb") as f:
            f.write(response.content)
        reader = PyPDF2.PdfReader("temp.pdf")
        text = "".join(page.extract_text() for page in reader.pages)
        logger.info(f"Extracted text from PDF: {url}")
        return text
    except Exception as e:
        logger.error(f"Error extracting PDF: {e}")
        return ""
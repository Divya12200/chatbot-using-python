import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    all_text = []
    for page in doc:
        all_text.append(page.get_text())  # Extracts text only
    return all_text






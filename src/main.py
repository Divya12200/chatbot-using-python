from src.pdf_reader import extract_text_from_pdf
from src.qa_module import QAModule

# Load PDF and initialize once
pdf_path = "data/Huezone_Product and Services_Brochure.pdf"  # use forward slashes or raw string
pdf_text = extract_text_from_pdf(pdf_path)
qa = QAModule(pdf_text)

# This function will be imported in app.py
def get_response(user_input):
    return qa.answer(user_input)


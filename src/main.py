from src.pdf_reader import extract_text_from_pdf
from src.qa_module import QAModule

# Load PDF once
pdf_path = "data/Huezone_Product and Services_Brochure.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
qa = QAModule(pdf_text)

def get_response(user_input):
    response, _ = qa.answer(user_input)
    return response





    


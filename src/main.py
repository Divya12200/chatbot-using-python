from src.pdf_reader import extract_text_from_pdf
from src.qa_module import QAModule

def main():
    pdf_path = "C:\python project\chatbot-using-python\data\Huezone_Product and Services_Brochure.pdf"
    pdf_text = extract_text_from_pdf(pdf_path)

    qa = QAModule(pdf_text)

    print("Chatbot Ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = qa.answer(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()

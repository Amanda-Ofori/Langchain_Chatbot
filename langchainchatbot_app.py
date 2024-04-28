# app.pystrea
import streamlit as st
from langchainchatbot_backend import PDFDocumentProcessor, CustomRAGProcessor

def main():
    st.title('Artificial Intelligence Chatbot')
    st.sidebar.title("Settings")
    directory = st.sidebar.text_input("Enter the directory of PDF files:", "path/to/pdf_directory")
    storage_directory = st.sidebar.text_input("Enter the directory for storing processed files:", "path/to/storage")
    model_name = st.sidebar.text_input("Enter the model name:", "gpt2")
    
    process_button = st.sidebar.button("Process PDFs")
    if process_button:
        processor = PDFDocumentProcessor(directory, storage_directory)
        processor.extract_text()
        st.success("PDFs processed and stored successfully.")
    
    query = st.text_input("Enter your question:")
    if st.button("Generate Answer"):
        if query:
            rag = CustomRAGProcessor(model_name, storage_directory)
            answer = rag.generate_answer(query)
            st.write("Answer:", answer)
        else:
            st.write("Please enter a question to generate an answer.")

if __name__ == "__main__":
    main()


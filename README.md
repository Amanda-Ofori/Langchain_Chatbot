# AI Chatbot using LangChain with Predefined PDFs
## Introduction

Welcome to our AI Chatbot project! This chatbot is built using LangChain, a framework for developing language-based applications. Our goal is to create a chatbot that can converse with users based on information extracted from predefined PDF documents. This project explores innovative methods to process and interpret the content within these documents, enabling the chatbot to provide informed and accurate responses to user queries.
Features

    Text Extraction: Utilizes PyMuPDF to extract text from PDF documents.
    Natural Language Understanding: Employs Hugging Face’s Transformers to process the extracted text and generate context-based answers.
    Web Interface: Features a Streamlit web interface for easy interaction with the chatbot.
    Advanced Query Handling: Incorporates techniques to manage large texts and token limitations of language models.

## Installation

Before you can run the chatbot, you need to set up your environment:

    Clone the Repository

    bash

git clone https://github.com/Amanda-Ofori/Langchain_Chatbot.git
cd Langchain_Chatbot

Install Dependencies
Ensure Python 3.6+ is installed, then run:

bash

    pip install -r requirements.txt

## Usage

To start the chatbot, run the Streamlit application:

bash

streamlit run app.py

Navigate to localhost:8501 in your web browser to interact with the chatbot. You can upload PDFs, extract text, and ask questions based on the extracted content.
Contributing

### Contributions to this project are welcome! Here’s how you can contribute:

    Reporting Bugs: Open an issue describing the bug.
    Suggesting Enhancements: Open an issue with your suggestions.
    Pull Requests: Submit your pull requests for new features or bug fixes.

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.
License

This project is licensed under the MIT License - see the LICENSE file for details.
## Acknowledgements

    LangChain: For providing the framework used in this project.
    Hugging Face's Transformers: For NLP models and tools.
    PyMuPDF: For handling PDF operations.

## Authors

    Amanda Ofori
    Yineteili Abii
    Kenneth Tetteh

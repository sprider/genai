import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import openai
import PyPDF2

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Initialize an empty knowledge base
knowledge_base = []

#  Read the OpenAI API key from the environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]


def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text


def generate_chatgpt_response(prompt):
    # Use the OpenAI GPT-3.5 model to generate a response based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-002", prompt=prompt, max_tokens=150
    )
    return response.choices[0].text.strip()


@app.route("/add_resume", methods=["POST"])
def add_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    resume_file = request.files["file"]
    if resume_file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:

        # Save the uploaded file to a temporary location
        tmp_file_path = "tmp_resume.pdf"
        resume_file.save(tmp_file_path)

        # Extract text from the uploaded resume
        resume_text = extract_text_from_pdf(tmp_file_path)
        
        # Remove the temporary file
        os.remove(tmp_file_path)

        # Add the resume data to the knowledge base
        resume_data = {"text": resume_text}
        knowledge_base.append(resume_data)
        
        return jsonify({"message": "Resume added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/query", methods=["POST"])
def query():
    user_query = request.json.get("query", "")

    try:
        # Get the latest resume text from the knowledge base
        latest_resume_text = knowledge_base[-1]["text"]

        # Combine user query and resume text as the prompt for ChatGPT
        prompt = f"User Query: {user_query}\nResume Text: {latest_resume_text}\n"

        # Generate a response using ChatGPT
        answer = generate_chatgpt_response(prompt)

        response = answer

    except Exception as e:
        response = "Error: " + str(e)

    return jsonify({"response": response}), 200


@app.route("/")
def hello():
    return "Hello, GenAI!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Local Installation and Testing Steps

**Clone the Repository**:
Clone the repository containing your Flask app code to your local machine.

**Set Up the Environment**:
Open a terminal and navigate to the project directory.

**Create a Virtual Environment**:
Create a virtual environment using `venv`. Run the following command:

```bash
python3 -m venv venv
```

**Activate the Virtual Environment**:
Activate the virtual environment using the following command:

```bash
source venv/bin/activate
```

**Install Required Packages**:
Make sure you have the required packages listed in the `requirements.txt` file. Install them using `pip`:

```bash
pip3 install -r requirements.txt
```

**Set Environment Variables**:
Add your OpenAI API key to the `.env` file located in the project directory. Open the `.env` file and set the `OPENAI_API_KEY` environment variable:

```
OPENAI_API_KEY=your_actual_api_key_here
```

Note: Replace `your_actual_api_key_here` with your real OpenAI API key.

**Run the Flask App**:
Now, you can run the Flask app using the following command:

```bash
python3 app.py
```

The app will start running, and you will see output indicating that the server is listening on `http://127.0.0.1:5000/`.

**Access the App**:
Open a web browser and navigate to `http://127.0.0.1:5000/`. You should see the homepage of your Flask app.

**Test the App**:
Interact with your Flask app through the browser or use tools like `curl` or Postman to test various routes and endpoints.

To test /add_resume API call, prepare a PDF resume that you want to upload. Then, use the following `curl` command:

```bash
curl -X POST -F "file=@path/to/resume.pdf" http://localhost:5000/add_resume
```

Replace `path/to/resume.pdf` with the actual path to the PDF resume you want to upload. The response will indicate whether the resume was added successfully.

To test /query API call, use the following `curl` command:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "Which companies has wattz worked for and in which city?"}' http://localhost:5000/query
```

Replace `"Which companies has wattz worked for and in which city?"` with the user's query you want to test. The response will be in JSON format, containing the relevant information from your knowledge base.

Make sure to have the correct URL (`http://localhost:5000`) and replace any placeholders (e.g., `"user_query"`, `"path/to/resume.pdf"`) with the actual query and file path you want to 
test.

The `curl` commands will interact with your Flask app's API endpoints, and the responses will be displayed in the command-line output. This way, you can verify the behavior and 
functionality of your GenAI application in a local environment.

**Deactivate the Virtual Environment**:
 When you are done testing the app, deactivate the virtual environment using the following command:

 ```bash
 deactivate
 ```

By following these steps, you can run and test your Flask app locally on your machine with the required environment variables set, including the `OPENAI_API_KEY` from the `.env` file.

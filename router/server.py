# app.py

from flask import Flask, request
import os
import requests

app = Flask(__name__)

executors = {
    "py": "http://python-executor:22221/execute",
    "java": "http://java-executor:22222/execute",
    "dart": "http://dart-executor:22223/execute"
}

@app.route('/upload', methods=['POST'])
def upload_code():
    file = request.files['file']
    lang = request.form.get('lang') # This should be the language extension (py, java, dart)
    filename = file.filename.rsplit('.', 1)[0] # Extracting filename without extension
    file.save(os.path.join("/tmp", f"{filename}.{lang}"))
    return "File Uploaded Successfully"

@app.route('/execute', methods=['GET'])
def execute_code():
    lang = request.args.get('lang') # This should be the language extension (py, java, dart)
    filename = request.args.get('filename') # Assume filename (without extension) is passed as a query parameter
    with open(os.path.join("/tmp", f"{filename}.{lang}"), 'r') as code_file:
        code = code_file.read()
        # Forward the code to the appropriate executor
        response = requests.post(executors[lang], data = code)
        return response.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22220)

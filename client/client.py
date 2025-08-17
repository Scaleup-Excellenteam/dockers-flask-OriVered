from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <form method="POST" action="/execute" enctype="multipart/form-data">
        File: <input type="file" name="file"><br>
        Language: <input type="text" name="lang" placeholder="py, java, dart"><br>
        <input type="submit" value="Execute">
    </form>
    '''

@app.route('/execute', methods=['POST'])
def execute():
    file = request.files['file']
    lang = request.form['lang']

    router_url = "http://localhost:22220"  # Assuming the router service is running on localhost port 5000

    # Upload the code file
    upload_response = requests.post(f"{router_url}/upload", files={"file": file}, data={"lang": lang})

    # The dictionary to hold the execution results for each language
    results = {"python": "", "java": "", "dart": ""}

    if upload_response.status_code == 200:
        for lang in results.keys():
            # Execute the code for each language
            execute_response = requests.get(f"{router_url}/execute", params={"lang": lang, "filename": file.filename})

            if execute_response.status_code == 200:
                # Save the execution output
                results[lang] = f"Execution output: <br> {execute_response.text}"
            else:
                results[lang] = f"Execution failed: <br> {execute_response.text}"
    else:
        return f"Upload failed: <br> {upload_response.text}"

    # Return the execution results for each language
    return "<br>".join(f"{lang}: {result}" for lang, result in results.items())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)  # Running this client on a different port to avoid conflict with the router service

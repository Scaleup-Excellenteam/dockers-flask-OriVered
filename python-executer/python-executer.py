
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    code = request.data.decode('utf-8')

    with open('main.py', 'w') as f:
        f.write(code)

    run_output = subprocess.run(['python3', 'main.py'], capture_output=True, text=True)

    return jsonify({'output': run_output.stdout if run_output.returncode == 0 else run_output.stderr})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)



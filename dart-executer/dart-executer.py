from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    code = request.data.decode('utf-8')

    with open('main.dart', 'w') as f:
        f.write(code)

    run_output = subprocess.run(['dart', 'main.dart'], capture_output=True, text=True)

    return jsonify({'output': run_output.stdout if run_output.returncode == 0 else run_output.stderr})

if __name__ == '__main__':
    app.run(debug=True)


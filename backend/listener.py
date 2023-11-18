from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/save-file', methods=['POST'])
def save_file():
    # Get the file from the request
    file = request.files['file']

    # Save the file to a directory
    file.save(file.filename)

    return 'File saved successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

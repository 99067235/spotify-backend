import json

from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/')
def hello():
    return 'Hello, World!'

def response(http_code, message):
    response = app.response_class(
        response=json.dumps(message),
        status=http_code,
        mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(debug=True)
import os
import requests
from flask import request, Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Home testing'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host='localhost', port=port)
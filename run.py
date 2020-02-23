import os
import requests
from flask import request, Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Home testing"

@app.route('/add',methods=['POST','GET'])
def add_carrier():
    varicle_number = input("Input varicle_number:")
    varicle_type = input("Input varicle_type(v1,v2,v3,v4,v5):")
    varicle_rate = input("Input varicle_number:")
    varicle_monthly_cycle_start = input("Input monthly_cycle_start:")
    varicle_monthly_cycle_end = input("Input varicle_monthly_cycle_end:")
    varicle_minimum_guranteee = input("Input varicle_minimum_guranteee:")
    context ={
        "varicle_number":varicle_number,
        "varicle_type":varicle_type,
        "varicle_rate":varicle_rate,
        "varicle_monthly_cycle_start":varicle_monthly_cycle_start,
        "varicle_monthly_cycle_end":varicle_monthly_cycle_end,
        "varicle_minimum_guranteee":varicle_minimum_guranteee
    }
    return context


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host='localhost', port=port)
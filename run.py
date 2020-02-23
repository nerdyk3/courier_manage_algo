import os
import requests
from flask import request, Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Home testing"

@app.route('/add',methods=['POST','GET'])
def add_carrier():
    """{
        "varicle_minimum_gurantee": "2400", 
        "varicle_monthly_cycle_end": "2/10/2019", 
        "varicle_monthly_cycle_start": "1/10/2019", 
        "varicle_number": "12", 
        "varicle_rate": "20", 
        "varicle_type": "v1"
        }"""
    varicle_number = input("Input varicle_number:")
    varicle_type = input("Input varicle_type(v1,v2,v3,v4,v5):")
    varicle_rate = input("Input varicle_rate / km:")
    varicle_monthly_cycle_start = input("Input monthly_cycle_start(DD/MM):")
    varicle_monthly_cycle_end = input("Input varicle_monthly_cycle_end(DD/MM):")
    varicle_minimum_gurantee = input("Input varicle_minimum_gurantee/km:")
    context ={
        "varicle_number":varicle_number,
        "varicle_type":varicle_type,
        "varicle_rate":varicle_rate,
        "varicle_monthly_cycle_start":varicle_monthly_cycle_start,
        "varicle_monthly_cycle_end":varicle_monthly_cycle_end,
        "varicle_minimum_gurantee":varicle_minimum_gurantee
    }
    with open('./data.json', 'a') as outfile:
        json.dump(context, outfile)
    return context

@app.route('/calculation',methods=['POST','GET'])
def rate_calculation():
    return "pass"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host='localhost', port=port)
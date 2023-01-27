import requests as r
import pandas as pd
import json


base_url = 'http://127.0.0.1:5000/' #base url local host

json_data = [
    {
    'Gender':'Male',
    'Married':'Yes',
    'Dependents':'1',
    'Education':'Graduate',
    'Self_Employed':'Yes',
    'ApplicantIncome':2000,
    'CoaplicantIncome':1000.0,
    'LoanAmount':400.0,
    'Loan_Amount_Term':240.0,
    'Credit_History':1.0,
    'Property_Area':'Urban'
    }
]

# Get Response
# response = r.get(base_url)
response = r.post(base_url + "predict", json = json_data)


if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print(response.json())
    print('request failed')
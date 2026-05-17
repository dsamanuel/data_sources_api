import requests
from requests.auth import HTTPBasicAuth

import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv() 


# Project Details
DOMAIN = os.getenv('DOMAIN')  # Replace with your CommCare domain
USERNAME = os.getenv('UNAME')
PASSWORD = os.getenv('PASSWORD')  # Use API Key here if 2FA is enabled
all_time_entries = []
# API Endpoint (example for cases)
url = f'https://www.commcarehq.org/a/{DOMAIN}/api/v0.5/case/'

def get_commcare_data():

    try:
        # requests.auth.HTTPBasicAuth encodes the credentials for you
        response = requests.get(
            url, 
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )
        
        if response.status_code == 200:
            print("Successfully authenticated!")
            return response.json()
        else:
            print(f"Failed: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    data = get_commcare_data()
    list_of_dicts = [dataj for dataj in data['objects'] if dataj.get('properties').get('case_type') =="participant"]

    d = len(list_of_dicts)

    for i in range(1, d):
        
        all_time_entries.append(list_of_dicts[i]['properties'])

    df = pd.DataFrame(all_time_entries)
    print(df.head())
import requests
import json
import os

from dotenv import load_dotenv


load_dotenv() 

# Configuration
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")
USERNAME = os.getenv("USERNAME")
URL = f"https://commcarehq.org/{DOMAIN}/api/v0.5/form/"

headers = {
    "Authorization": f"ApiKey {USERNAME}:{API_KEY}",
    "Content-Type": "application/json"
}

# Pulling data
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    # CommCare uses cursor pagination for large datasets
    #all_time_entries = [dataj for dataj in res['objects'] if dataj.get('form').get('@xmlns') == "http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495"]
    
    for dataj in data['objects']:
        print(dataj['form']['@xmlns'])
        #print(dataj['form']['@xmlns'] == "http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495")
else:
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")
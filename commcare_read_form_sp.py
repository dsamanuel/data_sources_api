import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv() 
# --- Configuration Constants ---
DOMAIN = os.getenv('MCDOMAIN')
API_KEY = os.getenv('MCAPI_KEY')
USERNAME = os.getenv('MCUSERNAME')

# Build the initial cases API URL (v2 is highly recommended)
# Source: https://commcare-hq.readthedocs.io/api/cases-v2.html
BASE_URL = f"https://www.commcarehq.org/a/{DOMAIN}/api/v0.5/form/"

# Construct headers for ApiKey authentication
# Format required: "ApiKey <email>:<api_key>"
HEADERS = {
    "Authorization": f"ApiKey {USERNAME}:{API_KEY}",
    "Content-Type": "application/json"
}
querystring = {'limit': 1000 }

def fetch_commcare_forms():
    """Loops through the pagination cursors to retrieve all records."""
    next_url = BASE_URL
    all_forms = []
    page_count = 1
    print(USERNAME, API_KEY, DOMAIN)  # Debug: Print credentials (remove in production)
    print("Starting data retrieval from CommCare...")

    while next_url and page_count <= 10:  # Ensure at least one request is made
        print(f"Fetching page {page_count}...")
        response = requests.get(next_url, headers=HEADERS, params=querystring)

        # Check for HTTP request errors
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code} - {response.text}")
            break

        data = response.json()
        
        # Extract metadata and individual case payloads
        meta = data.get("meta", {})
        #objects = data.get("objects", [])
        objects = [dataj for dataj in data['objects'] if dataj.get('form').get('@xmlns') == "http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495"]
        all_forms.extend(objects)
        
        # Cursor pagination handling 
        # CommCare returns a relative path or None in the 'next' field
        next_path = meta.get("next")
        if next_path:
            # Reconstruct full URL if path is relative
            if next_path.startswith("http"):
                next_url = next_path
            else:
                next_url = f"https://www.commcarehq.org/a/{DOMAIN}/api/v0.5/form/{next_path}"
            page_count += 1
        else:
            next_url = None  # End loop when no more pages exist

    print(f"Completed. Retracted a total of {len(all_forms)} forms.")
    return all_forms

if __name__ == "__main__":
    forms_data = fetch_commcare_forms()
    
    # Visual example of reading the top item
    if forms_data:
        df = pd.DataFrame(forms_data)
        df.to_csv("commcare_forms2.csv", index=False)  # Save to CSV for further analysis
        print("\nExample Form Preview:")
        print(f"Form Name: {forms_data[0].get('form').get('@name')}")
        print(f"Form Id: {forms_data[0].get('id')}")
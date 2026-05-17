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
BASE_URL = f"https://www.commcarehq.org/a/{DOMAIN}/api/v0.5/case/"

# Construct headers for ApiKey authentication
# Format required: "ApiKey <email>:<api_key>"
HEADERS = {
    "Authorization": f"ApiKey {USERNAME}:{API_KEY}",
    "Content-Type": "application/json"
}
query_params = {'limit': 100}  # Adjust limit as needed (max is typically 1000 for CommCare)

def fetch_commcare_cases():
    """Loops through the pagination cursors to retrieve all records."""
    next_url = BASE_URL
    all_cases = []
    page_count = 1
    print(USERNAME, API_KEY, DOMAIN)  # Debug: Print credentials (remove in production)
    print("Starting data retrieval from CommCare...")

    while next_url:  # Ensure at least one request is made
        print(f"Fetching page {page_count}...")
        response = requests.get(next_url, headers=HEADERS, params=query_params)

        # Check for HTTP request errors
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code} - {response.text}")
            break

        data = response.json()
        
        # Extract metadata and individual case payloads
        meta = data.get("meta", {})
        objects = data.get("objects", [])
        all_cases.extend(objects)
        
        # Cursor pagination handling 
        # CommCare returns a relative path or None in the 'next' field
        next_path = meta.get("next")
        if next_path:
            # Reconstruct full URL if path is relative
            if next_path.startswith("http"):
                next_url = next_path
            else:
                next_url = f"https://www.commcarehq.org/a/{DOMAIN}/api/v0.5/case/{next_path}"
            page_count += 1
        else:
            next_url = None  # End loop when no more pages exist

    print(f"Completed. Retracted a total of {len(all_cases)} cases.")
    return all_cases

if __name__ == "__main__":
    cases_data = fetch_commcare_cases()
    
    # Visual example of reading the top item
    if cases_data:
        df = pd.DataFrame(cases_data)
        df.to_csv("commcare_cases.csv", index=False)  # Save to CSV for further analysis
        print("\nExample Case Preview:")
        print(f"Case ID: {cases_data[0].get('case_id')}")
        print(f"Case Name: {cases_data[0].get('properties', {}).get('case_name')}")

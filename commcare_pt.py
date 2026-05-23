import requests
from requests.auth import HTTPDigestAuth
import os
from dotenv import load_dotenv
import uuid
from jinja2 import Template
from datetime import datetime, timezone
import uuid
import itertools
import xmltodict
import json
from dataclasses import dataclass
# 1. CommCare Configuration
load_dotenv()  # Load environment variables from .env file
DOMAIN = os.getenv("MCDOMAIN")
APP_ID = os.getenv("MCAPP_ID")
USERNAME = os.getenv("MCUSERNAME")
API_KEY = os.getenv("MCAPI_KEY")
MCUSER_ID = os.getenv("MCUSER_ID")

def now_utc() -> str:
    """
    Returns a UTC timestamp in ISO-8601 format with the offset as "Z".
    e.g. "2020-06-08T18:41:33.207Z"
    """
    now = datetime.now(tz=timezone.utc)
    now_iso = now.isoformat(timespec='milliseconds')
    now_iso_z = now_iso.replace('+00:00', 'Z')
    return now_iso_z
CASE_ID = uuid.uuid4().hex  # Generate a unique case ID
form_xmlns = "http://openrosa.org/formdesigner/9098B05D-1C43-4BF7-A4FE-E4A32E2CA2B6"
DEVICE_ID = "device123"  # Example device ID, replace as needed
# URL for Form Submission (Replace with your Domain and App ID)
url =  f'https://www.commcarehq.org/a/{DOMAIN}/api/case/v2/'



submission_id = uuid.uuid4().hex,
OWNER_ID = "41b373b43e484506be6efe90ccf7c065"  # Example owner ID, replace as needed

# 2. Define your OpenRosa XML Payload
# Ensure case_id and instanceID are unique UUIDs

jsson_payload = {
  
  "case_type": "icn",
  "case_name": "test test Harmon",
  "external_id": "13",
  "owner_id": f"{OWNER_ID}",
  
  
 
  
  
  "properties": {
    "name": "test test Harmon",
    "icn_title": "dsjlfjskdfd lkjfkdsjfkjdslkjf.",
    "icn_id": "898",
  },
  "indices": {
    "parent": {
      "case_id": "b00b2928-0324-45ae-8199-52d48d4d1710",
      "case_type": "implementing_agency",
      "relationship": "child"
    }
  }}


# 3. Headers and Payload structure
headers = {'Content-Type': 'application/json'}


# Step 2: Convert the dictionary to a JSON string

#xform = xml_payload #xtract the 'case' part of the JSON for submission



auth = (os.getenv('MCUSERNAME'), os.getenv('MCPASSWORD'))
# 4. Make the POST request using HTTP Digest Authentication
try:
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=jsson_payload,
                             headers=headers, auth=auth)
  
    # 5. Check the result
    if response.status_code in [200, 201]:
        print("Submission Successful!")
        print(f"Response: {response.text}")
    else:
        print(f"Failed to submit. Status Code: {response.status_code}")
        print(f"Error: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")



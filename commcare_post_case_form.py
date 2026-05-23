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
url =  f"https://www.commcarehq.org/a/{DOMAIN}/receiver/{APP_ID}/"



submission_id = uuid.uuid4().hex,
OWNER_ID = "41b373b43e484506be6efe90ccf7c065"  # Example owner ID, replace as needed

# 2. Define your OpenRosa XML Payload
# Ensure case_id and instanceID are unique UUIDs

xml_payload = f"""<?xml version="1.0" ?>
<data name="Register ICN"
      uiVersion="1"
      version="41"
      xmlns="{form_xmlns}">
  	<icn>
						<icn_id>{CASE_ID}</icn_id>
						<icn_title>djfkjdsljflkd</icn_title>
				
					
					</icn>
   <n0:case case_id="{CASE_ID}"
           date_modified="2020-06-08T18:41:33.207Z"
           user_id="de8cc5191f9b4e2a846069f0659fa35e"
           xmlns:n0="http://commcarehq.org/case/transaction/v2">
    <n0:create>
      <n0:case_name>GOUPAWEMEY, Moujid</n0:case_name>
      <n0:owner_id>{OWNER_ID}</n0:owner_id>
      <n0:case_type>icn</n0:case_type>
    </n0:create>
    <n0:update>
      <n0:case_location>9.2612578 0.7801739 0.0 500.0</n0:case_location>
      <n0:case_status>suspected</n0:case_status>
      <n0:family_name>KPIGMARE</n0:family_name>
      <n0:given_name>Didjate</n0:given_name>
      <n0:name_family_given>KPIGMARE, Didjate</n0:name_family_given>
      <n0:unique_id>KAR-BAS-306</n0:unique_id>
    </n0:update>
  </n0:case>
  <n1:meta xmlns:n1="http://openrosa.org/jr/xforms">
    <n1:deviceID>commcare_37478fd5-2730-4a14-a847-84e8848a1ff5</n1:deviceID>
    <n1:timeStart>2020-06-08T18:38:13.855Z</n1:timeStart>
    <n1:timeEnd>2020-06-08T18:41:33.207Z</n1:timeEnd>
    <n1:username>exampleuser</n1:username>
    <n1:userID>de8cc5191f9b4e2a846069f0659fa35e</n1:userID>
    <n1:instanceID>dca03509-4446-41dc-8352-2bb6f8516c7b</n1:instanceID>
    <n2:appVersion xmlns:n2="http://commcarehq.org/xforms">CommCare Version 2.48. Build 461457</n2:appVersion>
  </n1:meta>
</data>"""


# 3. Headers and Payload structure
headers = {'Content-Type': 'application/json'}


# Step 2: Convert the dictionary to a JSON string

#xform = xml_payload #xtract the 'case' part of the JSON for submission



auth = (os.getenv('MCUSERNAME'), os.getenv('MCPASSWORD'))
# 4. Make the POST request using HTTP Digest Authentication
try:
    headers = {'Content-Type': 'text/html; charset=UTF-8'}
    response = requests.post(url, xml_payload.encode('utf-8'),
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



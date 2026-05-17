import requests

# 1. Setup Configuration
DOMAIN = 'mc-ethiopia'
USERNAME = 'habtamuwhm@gmail.com'
API_KEY = 'd52fe25b11f90add3ef9b6217c64566a54c30eb0'
SUBMISSION_URL = f'https://commcarehq.org/a/{DOMAIN}/receiver/'

# 2. Define the XML Payload
# The XML structure should follow the CommCare CaseXML spec
xml_payload = """<?xml version='1.0' ?>
<data xmlns="http://openrosa.org">
    <meta>
        <username>hwoldeamanuel@mercycorps.org</username>
    </meta>
    <case case_id="unique-case-uuid" date_modified="2024-05-12T12:00:00Z" 
          user_id="8547a09562534861b235c00bb3c33991" xmlns="http://commcarehq.org">
        <create>
            <case_type>participant</case_type>
            <case_name>John Doe</case_name>
            <owner_id>your-user-id</owner_id>
        </create>
        <update>
            <phone_number>123456789</phone_number>
        </update>
    </case>
</data>
""".format(username=USERNAME)

# 3. Set Headers
headers = {
    'Content-Type': 'text/xml',
    'Authorization': f'ApiKey {USERNAME}:{API_KEY}'
}

# 4. Execute POST Request
try:
    response = requests.post(SUBMISSION_URL, data=xml_payload, headers=headers)
    
    if response.status_code == 201:
        print("Success: Data submitted to CommCare.")
    else:
        print(f"Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")

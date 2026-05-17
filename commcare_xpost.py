import requests
import uuid
from datetime import datetime
from requests.auth import HTTPBasicAuth


import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
# Project Details
DOMAIN = os.getenv('DOMAIN')  # Replace with your CommCare domain
USERNAME = os.getenv('UNAME')
PASSWORD = os.getenv('PASSWORD')  # Use API Key here if 2FA is enabled
TOKEN = os.getenv('TOKEN')  # If using API
# Receiver URL
# Use 'https://www.commcarehq.org/a/{DOMAIN}/receiver/' for a general submission
# Or include an APP_ID to tag it: 'https://www.commcarehq.org/a/{DOMAIN}/receiver/{APP_ID}/'
url = f'https://www.commcarehq.org/a/{DOMAIN}/receiver/'

# Generate unique IDs for the form and case
instance_id = str(uuid.uuid4())
case_id = str(uuid.uuid4())  # Use an existing case_id to UPDATE a case
current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

# Basic XML Form Structure (OpenRosa standard)
xml_data = """
				<data xmlns:jrm="http://dev.commcarehq.org/jr/xforms" xmlns="http://openrosa.org/formdesigner/8429F7E3-2CF2-4225-B54D-ABB7F95761B9" uiVersion="1" version="1" name="Participant Registration Form">
					<confirmation>
						<register_institution />
						<copy-1-of-instructions />
						<regional_program_name />
						<confirm_program />
						<owner_id />
					</confirmation>
					<participant_information>
						<first_name />
						<father_name />
						<grandfather_name />
						<participant_full_name />
						<gender />
						<registration_date />
					</participant_information>
					<date_of_birth>
						<participant_date_of_birth_unknown />
						<valid_dates1 />
						<valid_dates2 />
						<participant_date_of_birth />
						<age_component_math vellum:comment="This block computes the Calendar Distance in months and years between two days for age calculations. ">
							<in_dob vellum:comment="set the calculate condition for this field to the date of birth " />
							<in_today vellum:comment="Set the calculate condition for this field to be today's date (or the date of the record that is being collected)" />
							<dob_month vellum:comment="Calculation block: Do not change" />
							<today_months vellum:comment="Calculation block: Do not change" />
							<out_dob_years_old vellum:comment="Calculation block: Do not change" />
							<out_dob_months_old vellum:comment="Calculation block: Do not change" />
						</age_component_math>
						<participant_age>
							<what_is_the_participant_approximate_age />
							<participant_age_years />
							<participant_age_months />
						</participant_age>
						<normalized_age_details>
							<age_in_years />
							<age_in_months />
						</normalized_age_details>
					</date_of_birth>
					<participant_address>
						<participant_address />
						<ethregion />
						<ethzone />
						<ethworeda />
						<kebele />
					</participant_address>
					<participant_type>
						<participant_type />
						<participant_category />
					</participant_type>
					<participant_id>
						<manual_or_auto />
						<unique_case_id_manual />
						<auto_uid_label />
						<auto_uid />
						<unique_case_id />
						<participant_phone_number />
						<patient_phone_number_secondary />
						<created_by />
						<created_date />
					</participant_id>
				</data>"""

def post_to_commcare():
    try:
        response = requests.post(
            url,
            data=xml_data,
            headers={'Content-Type': 'text/xml'},
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )
        
        if response.status_code in [201, 202, 200]:
            print(f"Success! Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        else:
            print(f"Failed: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    post_to_commcare()

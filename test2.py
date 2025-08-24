import requests

from requests.auth import HTTPBasicAuth
import json
import pandas as pd
from io import StringIO
from datetime import datetime
import os
from dotenv import load_dotenv


#djflk
# Build paths inside the project like this: BASE_DIR / 'subdir'.




load_dotenv()  # This loads variables from .env into os.environ



url = os.getenv("base_url")+"customers"



params = {
    'authentication_token': 'E6Urjrvc4svlD5lAVA9VBBuhDmsxVqKEfpRmHw8Y488',
    'cursor':'LmVKd2x5ekVLd3pBTUFNQ3ZGTTFWa0JUWlZ2eU9qb1pnTEE4WjBrTGlUcUZfYjZIN0hWd0YydnNjcjcwZjYtWUY4cTFBRlNNTlduSGg0S2pKQmEzVmpwRTl6VEcyVkUwSzNIOXllNTc5R04zWE92NVZTQlNaa2NLREpRZkxORTlxdEtnVi1NQVgyOVVkeUEuQ3lLbVMyTkZlWVVLalZXamtlZjNTQVZLVVJB'
    }
headers = { 'Content-Type':"application/json", 
         
            'X-API-KEY': os.getenv("X_API_KEY"),
            'X-API-SECRET': os.getenv("X_API_SECRET"),
            "authentication_token" : os.getenv("authentication_token"),
           
        
           }

with requests.Session() as session:
    retry = Retry(
        total=5,
        status_forcelist=[500, 502, 503, 504],
        backoff_factor=0.1
    )
    session.mount(URL, HTTPAdapter(max_retries=retry))
    while True:
        (r := session.get(URL, params=params)).raise_for_status()
        data = r.json()
        for value in data['name']:
            orderID = value['customer_id']
           
           
           
            print(f'Order ID={orderID}')
        if (cursor := data.get('cursor')):
            params['cursor'] = cursor
        else:
            break

print("END")

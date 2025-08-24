import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

from itertools import chain

import requests
import os
from dotenv import load_dotenv

load_dotenv() 



url = os.getenv("base_url2")
headers = {'Authorization': os.getenv("auth")}

response = requests.get(url, headers=headers).json()

#data = response['data']
df = pd.json_normalize(response, record_path = ['data'])
#response = pd.json_normalize(response)
print(df)
df.to_csv('FDX150700024KB_records.csv')
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

from datetime import date, timedelta,datetime

start_date = date(2025, 7, 1)
end_date = datetime.now().date()
params = {
    'page': 1,
    'per_page': 3000,
}
format_start_date = start_date.strftime("%Y-%m-%d")
format_end_date = end_date.strftime("%Y-%m-%d")
base_url = os.getenv("base_url2")
url = f"{base_url}?from={format_start_date}&to={format_end_date}"

headers = {'Authorization': os.getenv("auth")}

response = requests.get(url, headers=headers).json()

#data = response['data']
df = pd.json_normalize(response, record_path = ['data'])

print(df)

#df.to_csv('devices.csv')
all_records = []  
for serial in df['serial']:
    serial = serial.strip()



    durl = f"{base_url}/{serial}/records?"



    while True:
    
   
        response = requests.get(durl, headers=headers, params=params).json()
        print(response)
        data = response['data']
        for item in data:
            item["serial"] = serial

        all_records.extend(data)
        
        if not response['data'] or len(response['data']) < params['per_page']:
            break
        
        params['page'] += 1



all_df = pd.DataFrame(all_records)
all_df.to_csv('all_devices_records.csv')


        

   

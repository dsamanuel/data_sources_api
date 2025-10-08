import requests

from datetime import datetime
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

from itertools import chain

import os

from dotenv import load_dotenv

load_dotenv() 
#djflk
# Build paths inside the project like this: BASE_DIR / 'subdir'.




 # This loads variables from .env into os.environ



def get_all_time_entries():
    
    base_url = os.getenv("comm_url")


   


    
    headers = { 
                "Content-Type":"application/json",
               
                "Authorization": os.getenv("comm_auth"),
                
       
           
        
           }
   
    #http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495', 
   
    querystring = {'limit': max(1000, 1) }


   
    # find out total number of pages
    res = requests.get(url=base_url, headers=headers, params=querystring).json()
    print(res)
    cursor = res.get('meta').get('next')
    print(cursor)
    #xl = res['objects'].get('form').get('@xmlns')
    #print(xl)
    #data = res['objects']
    all_time_entries = [dataj for dataj in res['objects'] if dataj.get('@xmlns') == "http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495"]
    
    #all_time_entries = datanew
    return all_time_entries
    
data = get_all_time_entries()
with open("output5.json", "w") as json_file:
    json.dump(data, json_file)
   
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import os
from itertools import chain

from dotenv import load_dotenv


#djflk
# Build paths inside the project like this: BASE_DIR / 'subdir'.




load_dotenv()  # This loads variables from .env into os.environ


def get_all_time_entries():
    base_url = os.getenv("base_url")+"customers" 

    
    headers = { 'Content-Type':"application/json", 
         
   'X-API-KEY': os.getenv("X_API_KEY"),
            'X-API-SECRET': os.getenv("X_API_SECRET"),
            "authentication_token" : os.getenv("authentication_token"),
           
        
           }
   

    querystring = {'reading_details': 'true','per_page':50  }



 

    # find out total number of pages
    res = res = requests.get(url=base_url,headers=headers, params=querystring).json()
    #total_pages = int(r['info']['pages'])
   
    cursor = res['cursor']   
    # results will be appended to this list
    all_time_entries = res['data']
    page = 1
    


    # loop through all pages and return JSON object
    while True:
        base_url = os.getenv("base_url")+"customers?cursor="+str(cursor)    

        
        headers = { 'Content-Type':"application/json", 
         
           'X-API-KEY': os.getenv("X_API_KEY"),
            'X-API-SECRET': os.getenv("X_API_SECRET"),
            "authentication_token" : os.getenv("authentication_token"),
           
        
           }    
        res = requests.get(url=base_url, headers=headers, params=querystring)
        resj = res.json()  
        cursor = resj['cursor']  
            
       
        list_of_dicts = resj['data']
        d = len(list_of_dicts)

        for i in range(1, d):
           all_time_entries.append(list_of_dicts[i])
                
        
       
        if not cursor:
            break 
        page = page + 1 
      
    # prettify JSON
    #datas = json.dumps(all_time_entries, sort_keys=True, indent=4)

    return all_time_entries

data = get_all_time_entries()

with open('alldata.json', 'w') as f:
    json.dump(data, f)
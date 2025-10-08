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
               
                "Authorization":os.getenv("comm_auth"),
                
       
           
        
           }
   
    #http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495', 
   
    querystring = {'limit': 1000 }


    page = 1
    
    # find out total number of pages
    res = requests.get(url=base_url, headers=headers, params=querystring).json()
    print(res)
    cursor = res.get('meta').get('next')
    print(cursor)
    #data = res['objects']
    all_time_entries = [dataj for dataj in res['objects'] if dataj.get('form').get('@xmlns') == "http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495"]
    
 
    #total_pages = int(r['info']['pages'])
    #with open("output.json", "w") as json_file:
    #    json.dump(res, json_file)
    while True:
        base_url = base_url+str(cursor)    

      
        headers = { 
                "Content-Type":"application/json",
               
                "Authorization": os.getenv("comm_auth"),
                
       
           
        
           } 

      

        res = requests.get(url=base_url, headers=headers, params=querystring).json()
        #print(page)
      
        cursor =  res.get('meta').get('next')
        print(cursor)
        #data = resj['objects']
        #datanew = [dataj for dataj in resj if dataj.get('@xmlns') == "http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495"]
        list_of_dicts = [dataj for dataj in res['objects'] if dataj.get('form').get('@xmlns') == "http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495"]
        
        
        d = len(list_of_dicts)

        for i in range(1, d):
           all_time_entries.append(list_of_dicts[i])
        
       
        if not cursor:
              break 
        page = page + 1

    return all_time_entries
  
data = get_all_time_entries()
df = pd.DataFrame(data)
df.to_csv("commcare_data.csv")


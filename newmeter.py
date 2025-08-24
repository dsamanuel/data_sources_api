import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import os
from dotenv import load_dotenv


#djflk
# Build paths inside the project like this: BASE_DIR / 'subdir'.




load_dotenv()  # This loads variables from .env into os.environ
url =  os.getenv("base_url")+"service_areas"






def get_all_time_entries():
    base_url = os.getenv("base_url")+"customers" 

    
    headers = { 'Content-Type':"application/json", 
         
            'X-API-KEY': os.getenv("X_API_KEY"),
            'X-API-SECRET': os.getenv("X_API_SECRET"),
            "authentication_token" : os.getenv("authentication_token"),
           
        
           }
   

   
    querystring = {'customer_only': True }


 

    # find out total number of pages
    res = requests.get(url=base_url,headers=headers,params=querystring)
    #total_pages = int(r['info']['pages'])
    result = res.json()
    cursor = result['cursor']   
    # results will be appended to this list
    #all_time_entries = res['data']
    page = 1
    
    #cust_df = pd.json_normalize(result, record_path = ['data'])
    meter_df = pd.json_normalize(data = result['data'], record_path = ['meters'],  meta=['id'], record_prefix='m_')

    # loop through all pages and return JSON object
    while True:
        base_url = os.getenv("base_url")+"customers?cursor="+str(cursor)    

      
        headers = { 'Content-Type':"application/json", 
         
          'X-API-KEY': os.getenv("X_API_KEY"),
            'X-API-SECRET': os.getenv("X_API_SECRET"),
            "authentication_token" : os.getenv("authentication_token"),
           } 

      

        res = requests.get(url=base_url, headers=headers,params=querystring)
        #print(page)
       
            
        result = res.json()

        cursor = result['cursor']

        #df_cust = pd.json_normalize(result, record_path = ['data'])
        df_meter = pd.json_normalize(data = result['data'], record_path = ['meters'], meta=['id'], record_prefix='m_')
        print(df_meter)
        #cust_df  =  pd.concat([cust_df, df_cust], ignore_index=True)
        meter_df  =  pd.concat([meter_df, df_meter], ignore_index=True)
        #print(page)
                
        
       
        if not cursor:
            break 
        page = page + 1 
      
    # prettify JSON
    #datas = json.dumps(all_time_entries, sort_keys=True, indent=4)

    return meter_df

meter_df = get_all_time_entries()
meter_df.to_csv('meterfdf.csv')

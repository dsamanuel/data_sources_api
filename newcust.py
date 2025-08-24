import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import os
from itertools import chain
from dotenv import load_dotenv

load_dotenv() 


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
    
    cust_df = pd.json_normalize(result, record_path = ['data'])
    #meter_df = pd.json_normalize(data = result['data'], record_path = ['meters'],  meta=['id'], record_prefix='m_')

    # loop through all pages and return JSON object
    while True:
        base_url =  os.getenv("base_url")+"customers?cursor="+str(cursor)    

      
        headers = { 'Content-Type':"application/json", 
         
          'X-API-KEY': os.getenv("X_API_KEY"),
            'X-API-SECRET': os.getenv("X_API_SECRET"),
            "authentication_token" : os.getenv("authentication_token"),
           } 

      

        res = requests.get(url=base_url, headers=headers,params=querystring)
        #print(page)
       
            
        result = res.json()

        cursor = result['cursor']

        df_cust = pd.json_normalize(result, record_path = ['data'])
        #df_meter = pd.json_normalize(data = result['data'], record_path = ['meters'], meta=['id'], record_prefix='m_')

        cust_df  =  pd.concat([cust_df, df_cust], ignore_index=True)
        #meter_df  =  pd.concat([meter_df, df_meter], ignore_index=True)
        #print(page)
                
        
       
        if not cursor:
            break 
        page = page + 1 
      
    # prettify JSON
    #datas = json.dumps(all_time_entries, sort_keys=True, indent=4)

    return cust_df

customers_df = get_all_time_entries()
customers_df.to_csv('custmer_df.csv')

'''

customers_df = pd.DataFrame(columns=['name', 'code', 'phone_number','id','serial','last_plan_renewal','next_plan_renewal','service_area_id','site_id','last_energy_limit_reset_at','last_energy_limit_reset_energy','energy_limited','balance_credit_value','balance_plan_value','balance_technical_debt_value'])

def lat(coord):
    if coord is None:
        lat = None
    else:
        lat = coord['latitude']
    
    return lat
def long(coord):
    if coord is None:
        long = None
    else:
        long = coord['longitude']
    
    return long
 
for i in range(0, len(data)):
    print(data[i])
    if data[i]['meters']:
        datac = {'name':data[i]['name'], 'code':data[i]['code'], 'phone_number':data[i]['phone_number'],'id':data[i]['id'],'serial':data[i]['meters'][0]['serial'],'last_plan_renewal':data[i]['last_plan_renewal'],'next_plan_renewal':data[i]['next_plan_renewal'],'service_area_id':data[i]['service_area_id'],'site_id':data[i]['site_id'], 'last_energy_limit_reset_at':data[i]['last_energy_limit_reset_at'], 'last_energy_limit_reset_energy':data[i]['last_energy_limit_reset_energy'], 'energy_limited':data[i]['energy_limited'],'balance_credit_value':data[i]['balances']['credit']['value'],'balance_plan_value':data[i]['balances']['plan']['value'],'balance_technical_debt_value':data[i]['balances']['technical_debt']['value']}
    else:
        datac = {'name':data[i]['name'], 'code':data[i]['code'], 'phone_number':data[i]['phone_number'],'id':data[i]['id'],'last_plan_renewal':data[i]['last_plan_renewal'],'next_plan_renewal':data[i]['next_plan_renewal'],'service_area_id':data[i]['service_area_id'],'site_id':data[i]['site_id'], 'last_energy_limit_reset_at':data[i]['last_energy_limit_reset_at'], 'last_energy_limit_reset_energy':data[i]['last_energy_limit_reset_energy'], 'energy_limited':data[i]['energy_limited'],'balance_credit_value':data[i]['balances']['credit']['value'],'balance_plan_value':data[i]['balances']['plan']['value'],'balance_technical_debt_value':data[i]['balances']['technical_debt']['value']} 
    
    cdf = pd.DataFrame(datac, index=[0])
    customers_df = pd.concat([customers_df, cdf], ignore_index=True)


#customer_df = customers_df[customers_df[['serial']].notnull().all(1)]
#customer_df = customer_df.drop_duplicates()
#customer_df= customer_df.reset_index(drop=True)
customers_df.to_csv('customer_final_df.csv', index=False)

'''
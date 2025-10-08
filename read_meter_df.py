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
        print(page)
        cursor = resj['cursor']  
            
       
        list_of_dicts = resj['data']
        d = len(list_of_dicts)

        for i in range(1, d):
           all_time_entries.append(list_of_dicts[i])
                
        
       
        if not cursor :
            break 
        page = page + 1 
      
    # prettify JSON
    #datas = json.dumps(all_time_entries, sort_keys=True, indent=4)

    return all_time_entries

data = get_all_time_entries()


meters_df = pd.DataFrame(columns=['cid','serial','address', "Latitude", 'Longitude', "operating_mode", "tariff_id","pole_id", "meter_phase", "apparent_power_avg", "current_avg","current_max", "current_min","energy", "frequency", "heartbeat_end", "heartbeat_start", "power_factor_avg", "state", "true_power_avg", "true_power_inst", "uptime_secs","user_power_limit", "voltage_avg","voltage_max", "voltage_min"])

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
   
    if data[i]['meters'] and data[i]['meters'][0]['latest_reading']:
        
        datam = {'cid': data[i]['id'],'serial':data[i]['meters'][0]['serial'],'address':data[i]['meters'][0]['address'], 'Latitude':lat(data[i]['meters'][0]['coordinates']), 'Longitude':long(data[i]['meters'][0]['coordinates']), 'operating_mode':data[i]['meters'][0]['operating_mode'], 'tariff_id':data[i]['meters'][0]['tariff_id'], 'pole_id':data[i]['meters'][0]['pole_id'], 'meter_phase':data[i]['meters'][0]['meter_phase'], 'apparent_power_avg':data[i]['meters'][0]['latest_reading']['apparent_power_avg'], 'current_avg':data[i]['meters'][0]['latest_reading']['current_avg'], 'current_max':data[i]['meters'][0]['latest_reading']['current_max'], 'current_min':data[i]['meters'][0]['latest_reading']['current_min'], 'energy':data[i]['meters'][0]['latest_reading']['energy'], 'frequency':data[i]['meters'][0]['latest_reading']['frequency'], 'heartbeat_end':data[i]['meters'][0]['latest_reading']['heartbeat_end'], 'heartbeat_start':data[i]['meters'][0]['latest_reading']['heartbeat_start'], 'power_factor_avg':data[i]['meters'][0]['latest_reading']['power_factor_avg'], 'state':data[i]['meters'][0]['latest_reading']['state'], 'true_power_avg':data[i]['meters'][0]['latest_reading']['true_power_avg'], 'true_power_inst':data[i]['meters'][0]['latest_reading']['true_power_inst'], 'uptime_secs':data[i]['meters'][0]['latest_reading']['uptime_secs'], 'user_power_limit':data[i]['meters'][0]['latest_reading']['user_power_limit'], 'voltage_avg':data[i]['meters'][0]['latest_reading']['voltage_avg'], 'voltage_max':data[i]['meters'][0]['latest_reading']['voltage_max'], 'voltage_min':data[i]['meters'][0]['latest_reading']['voltage_min']}
    else:
        datam = {'cid': data[i]['id'],'serial':data[i]['meters'][0]['serial'],'address':data[i]['meters'][0]['address'], 'Latitude':lat(data[i]['meters'][0]['coordinates']), 'Longitude':long(data[i]['meters'][0]['coordinates']), 'operating_mode':data[i]['meters'][0]['operating_mode'], 'tariff_id':data[i]['meters'][0]['tariff_id'], 'pole_id':data[i]['meters'][0]['pole_id'], 'meter_phase':data[i]['meters'][0]['meter_phase'], 'apparent_power_avg':None, 'current_avg':None, 'current_max':None, 'current_min':None, 'energy':None, 'frequency':None, 'heartbeat_end':None, 'heartbeat_start':None, 'power_factor_avg':None, 'state':None, 'true_power_avg':None, 'true_power_inst':None, 'uptime_secs':None, 'user_power_limit':None, 'voltage_avg':None, 'voltage_max':None, 'voltage_min':None}
    
    
    mdf = pd.DataFrame(datam, index=[0])
    if mdf.empty:
    
        meters_df = meters_df.copy()
    else:
        meters_df = pd.concat([meters_df, mdf], ignore_index=True)   
        #jdf = pd.json_normalize(j, max_level=3)
        #meter_df = pd.concat([meter_df, jdf], ignore_index=True)

meter_df = meters_df[meters_df[['serial']].notnull().all(1)]
meter_df = meter_df.drop_duplicates()
meter_df = meter_df.reset_index(drop=True)

print(meter_df)

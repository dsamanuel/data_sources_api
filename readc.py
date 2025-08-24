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
   

    querystring = {'reading_details': 'true', 'per_page':50,  }



 

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
         
           'X-API-KEY': 'pV1BfY-PSvF6JIB1tJ5GIqSNdzQTblUanEqS2OENDKk',
           'X-API-SECRET': "u%%%*FwGekfYAtW%a2DihZNu@P^k5^2Y",
           
        
           }    
        res = requests.get(url=base_url, headers=headers, params=querystring)
        resj = res.json()  
        cursor = resj['cursor']  
            
       
        list_of_dicts = resj['data']
        d = len(list_of_dicts)

        for i in range(1, d):
           all_time_entries.append(list_of_dicts[i])
                
        
        page = page + 1 
        if not cursor:
            break 
       

    # prettify JSON
    #datas = json.dumps(all_time_entries, sort_keys=True, indent=4)

    return all_time_entries

data = get_all_time_entries()


reading_df = pd.DataFrame(columns=['current_max',	'true_power_avg',	'frequency',	'voltage_min',	
                                'voltage_avg',	'kilowatt_hours_period',	'heartbeat_end',	'rate',	
                                'current_min',	'current_avg',	'true_power_inst',	'state',	
                                'user_power_limit',	'energy',	'voltage_max',	'meter/serial',	
                                'meter/customer/code',	'meter/customer/name',	'meter/customer/id',	
                                'apparent_power_avg',	'uptime',	'heartbeat_start',	'power_factor_avg',
                                'tou_modifier',	'site',	'kilowatt_hours',	'_uncertain_metadata'])


for i in range(0, len(data)):
        if data[i]['meters'] and data[i]['meters'][0]['latest_reading']:
                datar = { 'current_max':data[i]['meters'][0]['latest_reading']['current_max'],	'true_power_avg':data[i]['meters'][0]['latest_reading']['true_power_avg'],'frequency':data[i]['meters'][0]['latest_reading']['frequency'],
                         'voltage_min':data[i]['meters'][0]['latest_reading']['voltage_min'],	'voltage_avg':data[i]['meters'][0]['latest_reading']['voltage_avg'],		'heartbeat_end':data[i]['meters'][0]['latest_reading']['heartbeat_end'],		
                         'current_min':data[i]['meters'][0]['latest_reading']['current_min'],	'current_avg':data[i]['meters'][0]['latest_reading']['current_avg'],	'true_power_inst':data[i]['meters'][0]['latest_reading']['true_power_inst'],	'state':data[i]['meters'][0]['latest_reading']['state'],
                         'user_power_limit':data[i]['meters'][0]['latest_reading']['user_power_limit'],	'energy':data[i]['meters'][0]['latest_reading']['energy'],	'voltage_max':data[i]['meters'][0]['latest_reading']['voltage_max'],	'meter/serial':data[i]['meters'][0]['serial'],	
                         'meter/customer/code':data[i]['code'],	'meter/customer/name':data[i]['name'],	'meter/customer/id':data[i]['id'],	'apparent_power_avg':data[i]['meters'][0]['latest_reading']['apparent_power_avg'],	
                         'uptime':data[i]['meters'][0]['latest_reading']['uptime_secs'],	'heartbeat_start':data[i]['meters'][0]['latest_reading']['heartbeat_start'],	'power_factor_avg':data[i]['meters'][0]['latest_reading']['power_factor_avg'],
                         	'site':data[i]['site_id']
                        }
                
                rdf = pd.DataFrame(datar, index=[0])
 
                #meter_df = pd.concat([meter_df, mdf], ignore_index=True)   
                reading_df = pd.concat([reading_df, rdf], ignore_index=True)

reading_df = reading_df
print(reading_df)

# customer_df = pd.DataFrame(columns=['name', 'code', 'phone_number','id','serial','last_plan_renewal','next_plan_renewal','service_area_id','site_id','last_energy_limit_reset_at','last_energy_limit_reset_energy','energy_limited','balance_credit_value','balance_plan_value','balance_technical_debt_value'])
# meter_df = pd.DataFrame(columns=['cid','serial','address', "Latitude", 'Longitude', "operating_mode", "tariff_id","pole_id", "meter_phase", "apparent_power_avg", "current_avg","current_max", "current_min","energy", "frequency", "heartbeat_end", "heartbeat_start", "power_factor_avg", "state", "true_power_avg", "true_power_inst", "uptime_secs","user_power_limit", "voltage_avg","voltage_max", "voltage_min"])

# def lat(coord):
#     if coord is None:
#         lat = None
#     else:
#         lat = coord['latitude']
    
#     return lat
# def long(coord):
#     if coord is None:
#         long = None
#     else:
#         long = coord['longitude']
    
#     return long
 
# for i in range(0, len(data)):
#     datac = {'name':data[i]['name'], 'code':data[i]['code'], 'phone_number':data[i]['phone_number'],'id':data[i]['id'],'serial':data[i]['meters'][0]['serial'],'last_plan_renewal':data[i]['last_plan_renewal'],'next_plan_renewal':data[i]['next_plan_renewal'],'service_area_id':data[i]['service_area_id'],'site_id':data[i]['site_id'], 'last_energy_limit_reset_at':data[i]['last_energy_limit_reset_at'], 'last_energy_limit_reset_energy':data[i]['last_energy_limit_reset_energy'], 'energy_limited':data[i]['energy_limited'],'balance_credit_value':data[i]['balances']['credit']['value'],'balance_plan_value':data[i]['balances']['plan']['value'],'balance_technical_debt_value':data[i]['balances']['technical_debt']['value']}
#     cdf = pd.DataFrame(datac, index=[0])
 
#     #cdf = pd.DataFrame.from_dict(datac, orient = 'columns')
#     customer_df = pd.concat([customer_df, cdf], ignore_index=True)
#     if data[i]['meters'][0]['latest_reading']:
        
#         datam = {'cid': data[i]['id'],'serial':data[i]['meters'][0]['serial'],'address':data[i]['meters'][0]['address'], 'Latitude':lat(data[i]['meters'][0]['coordinates']), 'Longitude':long(data[i]['meters'][0]['coordinates']), 'operating_mode':data[i]['meters'][0]['operating_mode'], 'tariff_id':data[i]['meters'][0]['tariff_id'], 'pole_id':data[i]['meters'][0]['pole_id'], 'meter_phase':data[i]['meters'][0]['meter_phase'], 'apparent_power_avg':data[i]['meters'][0]['latest_reading']['apparent_power_avg'], 'current_avg':data[i]['meters'][0]['latest_reading']['current_avg'], 'current_max':data[i]['meters'][0]['latest_reading']['current_max'], 'current_min':data[i]['meters'][0]['latest_reading']['current_min'], 'energy':data[i]['meters'][0]['latest_reading']['energy'], 'frequency':data[i]['meters'][0]['latest_reading']['frequency'], 'heartbeat_end':data[i]['meters'][0]['latest_reading']['heartbeat_end'], 'heartbeat_start':data[i]['meters'][0]['latest_reading']['heartbeat_start'], 'power_factor_avg':data[i]['meters'][0]['latest_reading']['power_factor_avg'], 'state':data[i]['meters'][0]['latest_reading']['state'], 'true_power_avg':data[i]['meters'][0]['latest_reading']['true_power_avg'], 'true_power_inst':data[i]['meters'][0]['latest_reading']['true_power_inst'], 'uptime_secs':data[i]['meters'][0]['latest_reading']['uptime_secs'], 'user_power_limit':data[i]['meters'][0]['latest_reading']['user_power_limit'], 'voltage_avg':data[i]['meters'][0]['latest_reading']['voltage_avg'], 'voltage_max':data[i]['meters'][0]['latest_reading']['voltage_max'], 'voltage_min':data[i]['meters'][0]['latest_reading']['voltage_min']}
#     else:
#         datam = {'cid': data[i]['id'],'serial':data[i]['meters'][0]['serial'],'address':data[i]['meters'][0]['address'], 'Latitude':lat(data[i]['meters'][0]['coordinates']), 'Longitude':long(data[i]['meters'][0]['coordinates']), 'operating_mode':data[i]['meters'][0]['operating_mode'], 'tariff_id':data[i]['meters'][0]['tariff_id'], 'pole_id':data[i]['meters'][0]['pole_id'], 'meter_phase':data[i]['meters'][0]['meter_phase'], 'apparent_power_avg':None, 'current_avg':None, 'current_max':None, 'current_min':None, 'energy':None, 'frequency':None, 'heartbeat_end':None, 'heartbeat_start':None, 'power_factor_avg':None, 'state':None, 'true_power_avg':None, 'true_power_inst':None, 'uptime_secs':None, 'user_power_limit':None, 'voltage_avg':None, 'voltage_max':None, 'voltage_min':None}
#     mdf = pd.DataFrame(datam, index=[0])
#     meter_df = pd.concat([meter_df, mdf], ignore_index=True)   
#     #for j in i['meters']:
#         #jdf = pd.json_normalize(j, max_level=3)
#         #meter_df = pd.concat([meter_df, jdf], ignore_index=True)
# meter_df = meter_df.drop_duplicates()
# print(meter_df)
# customer_df = customer_df.drop_duplicates()

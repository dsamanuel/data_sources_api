import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import os
from dotenv import load_dotenv


#djflk
# Build paths inside the project like this: BASE_DIR / 'subdir'.




load_dotenv()  # This loads variables from .env into os.environ



url = os.getenv("base_url")+"customers"



headers = { 'Content-Type':"application/json", 
         
           'X-API-KEY': os.getenv("X_API_KEY"),
            'X-API-SECRET': os.getenv("X_API_SECRET"),
            "authentication_token" : os.getenv("authentication_token"),
           }

querystring = {'reading_details': 'true', 'per_page':50  }


res = requests.get(url=url,headers=headers, params=querystring)
result = res.json()



data = result['data']

reading_df = pd.DataFrame(columns=['current_max',	'true_power_avg',	'frequency',	'voltage_min',	'voltage_avg',	'kilowatt_hours_period',	'heartbeat_end',	'rate',	'current_min',	'current_avg',	'true_power_inst',	'state',	'user_power_limit',	'energy',	'voltage_max',	'serial',	'meter/customer/code',	'meter/customer/name',	'meter/customer/id',	'apparent_power_avg',	'uptime',	'heartbeat_start',	'power_factor_avg',	'tou_modifier',	'site',	'kilowatt_hours'])

for i in range(0, len(data)):
        if data[i]['meters'][0]['latest_reading']:
                datar = { 'current_max':data[i]['meters'][0]['latest_reading']['current_max'],	'true_power_avg':data[i]['meters'][0]['latest_reading']['true_power_avg'],'frequency':data[i]['meters'][0]['latest_reading']['frequency'],
                         'voltage_min':data[i]['meters'][0]['latest_reading']['current_max'],	'voltage_avg':data[i]['meters'][0]['latest_reading']['voltage_avg'],		'heartbeat_end':data[i]['meters'][0]['latest_reading']['heartbeat_end'],		'current_min':data[i]['meters'][0]['latest_reading']['current_min'],	'current_avg':data[i]['meters'][0]['latest_reading']['current_avg'],	'true_power_inst':data[i]['meters'][0]['latest_reading']['true_power_inst'],	'state':data[i]['meters'][0]['latest_reading']['state'],	'user_power_limit':data[i]['meters'][0]['latest_reading']['user_power_limit'],	'energy':data[i]['meters'][0]['latest_reading']['energy'],	'voltage_max':data[i]['meters'][0]['latest_reading']['voltage_max'],	'serial':data[i]['meters'][0]['serial'],	'meter/customer/code':data[i]['code'],	'meter/customer/name':data[i]['name'],	'meter/customer/id':data[i]['id'],	'apparent_power_avg':data[i]['meters'][0]['latest_reading']['apparent_power_avg'],	'voltage_avg':data[i]['meters'][0]['latest_reading']['voltage_avg'],		'heartbeat_end':data[i]['meters'][0]['latest_reading']['heartbeat_end'],		'current_min':data[i]['meters'][0]['latest_reading']['current_min'],	'current_avg':data[i]['meters'][0]['latest_reading']['current_avg'],	'true_power_inst':data[i]['meters'][0]['latest_reading']['true_power_inst'],	'state':data[i]['meters'][0]['latest_reading']['state'],	'user_power_limit':data[i]['meters'][0]['latest_reading']['user_power_limit'],	'energy':data[i]['meters'][0]['latest_reading']['energy'],	'voltage_max':data[i]['meters'][0]['latest_reading']['voltage_max'],	'serial':data[i]['meters'][0]['serial'],	'meter/customer/code':data[i]['code'],	'meter/customer/name':data[i]['name'],	'meter/customer/id':data[i]['id'],	'apparent_power_avg':data[i]['meters'][0]['latest_reading']['current_max'],		'heartbeat_start':data[i]['meters'][0]['latest_reading']['heartbeat_start'],	'power_factor_avg':data[i]['meters'][0]['latest_reading']['power_factor_avg'],		
                        	'uptime':data[i]['meters'][0]['latest_reading']['uptime_secs'],	'heartbeat_start':data[i]['meters'][0]['latest_reading']['heartbeat_start'],	'power_factor_avg':data[i]['meters'][0]['latest_reading']['power_factor_avg'],		'site':data[i]['site_id'],
                        }
                
                rdf = pd.DataFrame(datar, index=[0])
 
                #meter_df = pd.concat([meter_df, mdf], ignore_index=True)   
                reading_df = pd.concat([reading_df, rdf], ignore_index=True)

print(reading_df)
#json_object = json.dumps(data, indent = 4)

#json_object.to_json('datass.json', orient='records', lines=True)
#dataset = pd.json_normalize(data,max_level=2)
""" 
customer_df = pd.DataFrame(columns=['name', 'code', 'phone_number','id','serial','last_plan_renewal','next_plan_renewal','service_area_id','site_id','last_energy_limit_reset_at','last_energy_limit_reset_energy','energy_limited','balance_credit_value','balance_plan_value','balance_technical_debt_value'])
meter_df = pd.DataFrame(columns=['cid','serial','address', "Latitude", 'Longitude', "operating_mode", "tariff_id","pole_id", "meter_phase", "apparent_power_avg", "current_avg","current_max", "current_min","energy", "frequency", "heartbeat_end", "heartbeat_start", "power_factor_avg", "state", "true_power_avg", "true_power_inst", "uptime_secs","user_power_limit", "voltage_avg","voltage_max", "voltage_min"])

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
    datac = {'name':data[i]['name'], 'code':data[i]['code'], 'phone_number':data[i]['phone_number'],'id':data[i]['id'],'serial':data[i]['meters'][0]['serial'],'last_plan_renewal':data[i]['last_plan_renewal'],'next_plan_renewal':data[i]['next_plan_renewal'],'service_area_id':data[i]['service_area_id'],'site_id':data[i]['site_id'], 'last_energy_limit_reset_at':data[i]['last_energy_limit_reset_at'], 'last_energy_limit_reset_energy':data[i]['last_energy_limit_reset_energy'], 'energy_limited':data[i]['energy_limited'],'balance_credit_value':data[i]['balances']['credit']['value'],'balance_plan_value':data[i]['balances']['plan']['value'],'balance_technical_debt_value':data[i]['balances']['technical_debt']['value']}
    cdf = pd.DataFrame(datac, index=[0])
 
    #cdf = pd.DataFrame.from_dict(datac, orient = 'columns')
    customer_df = pd.concat([customer_df, cdf], ignore_index=True)
    datam = {'cid': data[i]['id'],'serial':data[i]['meters'][0]['serial'],'address':data[i]['meters'][0]['address'], 'Latitude':lat(data[i]['meters'][0]['coordinates']), 'Longitude':long(data[i]['meters'][0]['coordinates']), 'operating_mode':data[i]['meters'][0]['operating_mode'], 'tariff_id':data[i]['meters'][0]['tariff_id'], 'pole_id':data[i]['meters'][0]['pole_id'], 'meter_phase':data[i]['meters'][0]['meter_phase'], 'apparent_power_avg':data[i]['meters'][0]['latest_reading']['apparent_power_avg'], 'current_avg':data[i]['meters'][0]['latest_reading']['current_avg'], 'current_max':data[i]['meters'][0]['latest_reading']['current_max'], 'current_min':data[i]['meters'][0]['latest_reading']['current_min'], 'energy':data[i]['meters'][0]['latest_reading']['energy'], 'frequency':data[i]['meters'][0]['latest_reading']['frequency'], 'heartbeat_end':data[i]['meters'][0]['latest_reading']['heartbeat_end'], 'heartbeat_start':data[i]['meters'][0]['latest_reading']['heartbeat_start'], 'power_factor_avg':data[i]['meters'][0]['latest_reading']['power_factor_avg'], 'state':data[i]['meters'][0]['latest_reading']['state'], 'true_power_avg':data[i]['meters'][0]['latest_reading']['true_power_avg'], 'true_power_inst':data[i]['meters'][0]['latest_reading']['true_power_inst'], 'uptime_secs':data[i]['meters'][0]['latest_reading']['uptime_secs'], 'user_power_limit':data[i]['meters'][0]['latest_reading']['user_power_limit'], 'voltage_avg':data[i]['meters'][0]['latest_reading']['voltage_avg'], 'voltage_max':data[i]['meters'][0]['latest_reading']['voltage_max'], 'voltage_min':data[i]['meters'][0]['latest_reading']['voltage_min']}
  
    mdf = pd.DataFrame(datam, index=[0])
    meter_df = pd.concat([meter_df, mdf], ignore_index=True)   
    #for j in i['meters']:
        #jdf = pd.json_normalize(j, max_level=3)
        #meter_df = pd.concat([meter_df, jdf], ignore_index=True)
print(meter_df)
meter_df.to_csv('meterdfss.csv', index=False)
 """

""" def llst1(loadlimit, ty):
    if loadlimit['type'] == 'scheduled':
        if ty == 0:
            return loadlimit['value'][0]['start_time']
        elif ty == 1:
            return loadlimit['value'][0]['load_limit']
   
    elif loadlimit['type'] == 'flat':
        if ty == 2:
            return loadlimit['value']
        else:
            return None
def llst2(loadlimit, ty):
    if loadlimit['type'] == 'scheduled':
        if ty == 0:
            return loadlimit['value'][1]['start_time']
        else:
            return loadlimit['value'][1]['load_limit']
    else:
        return None
json_object = json.dumps(data, indent = 4)

tarrif_df = pd.DataFrame(columns=["id","name","electricity_rate","start_time1","modifier1","start_time2","modifier2","type","flat_value","load_limit_st1","load_limit_st1_v","load_limit_st2","load_limit_st2_v","low_balance_threshold","inrush_current_protection_disabled","block_rate","electricity_rate_type","block_rate_cycle_reset_energy","last_block_rate_cycle_reset_at","daily_energy_limit","daily_energy_limit_unit"])

for i in range(0, len(data)):
   
    datat = {'id':data[i]['id'],'name':data[i]['name'],'electricity_rate':data[i]['electricity_rate']['value'], 'start_time1':data[i]['time_of_use'][0]['start_time'],'modifier1':data[i]['time_of_use'][0]['modifier'],'start_time2':data[i]['time_of_use'][1]['start_time'], 'modifier2':data[i]['time_of_use'][1]['modifier'],"type":data[i]['load_limit']['type'],"flat_value":llst1(data[i]['load_limit'],2),"load_limit_st1":llst1(data[i]['load_limit'],0),"load_limit_st1_v":llst1(data[i]['load_limit'],1),"load_limit_st2":llst2(data[i]['load_limit'],0),"load_limit_st2_v":llst2(data[i]['load_limit'],1),'low_balance_threshold':data[i]['low_balance_threshold'],'inrush_current_protection_disabled':data[i]['inrush_current_protection_disabled'],'block_rate':data[i]['block_rate'],'electricity_rate_type':data[i]['electricity_rate_type'],'block_rate_cycle_reset_energy':data[i]['block_rate_cycle_reset_energy'],'last_block_rate_cycle_reset_at':data[i]['last_block_rate_cycle_reset_at'],'daily_energy_limit':data[i]['daily_energy_limit'],'daily_energy_limit_unit':data[i]['daily_energy_limit_unit']}
    tdf = pd.DataFrame(datat, index=[0])
    tarrif_df = pd.concat([tarrif_df, tdf], ignore_index=True)

tarrif_df.to_csv('tasrrif_df.csv', index=False) """
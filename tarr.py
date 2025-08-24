import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import os
from dotenv import load_dotenv


#djflk
# Build paths inside the project like this: BASE_DIR / 'subdir'.




load_dotenv()  # This loads variables from .env into os.environ


url = os.getenv("base_url")+"tariffs"



headers = { 'Content-Type':"application/json", 
         
            'X-API-KEY': os.getenv("X_API_KEY"),
            'X-API-SECRET': os.getenv("X_API_SECRET"),
            "authentication_token" : os.getenv("authentication_token"),
           }

querystring = {'reading_details': 'true', 'per_page':50 }


res = requests.get(url=url,headers=headers)
result = res.json()



data = result['data']
print(data)

'''
def llst1(loadlimit, ty):
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
    if data[i]['name'] == "Null":
        
        datat = {'id':data[i]['id'],'name':"Unspecified",'electricity_rate':data[i]['electricity_rate']['value'], 'start_time1':data[i]['time_of_use'][0]['start_time'],'modifier1':data[i]['time_of_use'][0]['modifier'],'start_time2':data[i]['time_of_use'][1]['start_time'], 'modifier2':data[i]['time_of_use'][1]['modifier'],"type":data[i]['load_limit']['type'],"flat_value":llst1(data[i]['load_limit'],2),"load_limit_st1":llst1(data[i]['load_limit'],0),"load_limit_st1_v":llst1(data[i]['load_limit'],1),"load_limit_st2":llst2(data[i]['load_limit'],0),"load_limit_st2_v":llst2(data[i]['load_limit'],1),'low_balance_threshold':data[i]['low_balance_threshold'],'inrush_current_protection_disabled':data[i]['inrush_current_protection_disabled'],'block_rate':data[i]['block_rate'],'electricity_rate_type':data[i]['electricity_rate_type'],'block_rate_cycle_reset_energy':data[i]['block_rate_cycle_reset_energy'],'last_block_rate_cycle_reset_at':data[i]['last_block_rate_cycle_reset_at'],'daily_energy_limit':data[i]['daily_energy_limit'],'daily_energy_limit_unit':data[i]['daily_energy_limit_unit']}
        tdf = pd.DataFrame(datat, index=[0])
    else:
        datat = {'id':data[i]['id'],'name':data[i]['name'],'electricity_rate':data[i]['electricity_rate']['value'], 'start_time1':data[i]['time_of_use'][0]['start_time'],'modifier1':data[i]['time_of_use'][0]['modifier'],'start_time2':data[i]['time_of_use'][1]['start_time'], 'modifier2':data[i]['time_of_use'][1]['modifier'],"type":data[i]['load_limit']['type'],"flat_value":llst1(data[i]['load_limit'],2),"load_limit_st1":llst1(data[i]['load_limit'],0),"load_limit_st1_v":llst1(data[i]['load_limit'],1),"load_limit_st2":llst2(data[i]['load_limit'],0),"load_limit_st2_v":llst2(data[i]['load_limit'],1),'low_balance_threshold':data[i]['low_balance_threshold'],'inrush_current_protection_disabled':data[i]['inrush_current_protection_disabled'],'block_rate':data[i]['block_rate'],'electricity_rate_type':data[i]['electricity_rate_type'],'block_rate_cycle_reset_energy':data[i]['block_rate_cycle_reset_energy'],'last_block_rate_cycle_reset_at':data[i]['last_block_rate_cycle_reset_at'],'daily_energy_limit':data[i]['daily_energy_limit'],'daily_energy_limit_unit':data[i]['daily_energy_limit_unit']}
        tdf = pd.DataFrame(datat, index=[0])
    tarrif_df = pd.concat([tarrif_df, tdf], ignore_index=True)


'''
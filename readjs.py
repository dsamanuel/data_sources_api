import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

from itertools import chain


df = pd.read_json('ss.json')
print(df.info())

'''
with open('ss.json') as user_file:
  data = user_file.read()

for i in range(0, len(data)):
    print(i[0])
        

   

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
customer_df= customers_df.reset_index(drop=True)
customer_df.to_csv('customer_final_df.csv', index=False)

'''
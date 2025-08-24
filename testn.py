import requests

from requests.auth import HTTPBasicAuth
import json

import os
from pathlib import Path
import pandas as pd

#djflk
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

# accessing and printing value



url =  os.getenv("base_url")+"service_areas"



headers = { 'Content-Type':"application/json", 
         
           'X-API-KEY': os.getenv("X_API_KEY"),
            'X-API-SECRET': os.getenv("X_API_SECRET"),
            "authentication_token" : os.getenv("authentication_token"),
           }
querystring = {'insights_details': True }

res = requests.get(url=url,headers=headers,params=querystring)
result = res.json()

df = pd.json_normalize(result, record_path = ['data'])

print(df)


"""
querystring = {'customer_only': True }


res = requests.get(url=url,headers=headers,params=querystring)
result = res.json()

df = pd.json_normalize(result, record_path = ['data'])
df_meter = pd.json_normalize(data = result['data'], record_path = ['meters'])

df_meter.to_csv('mymeter.csv')


data = result['data']

json_str = json.dumps(data)
# displaying



with open("mydata.json", "w") as final:
	json.dump(json_str, final)

print(res)


ss = result['data']
print(ss)


time_use = []
print(type(time_use))

for i in range(0, len(ss)):
    time_uses = ss[i]['time_of_use']
    print(len(time_uses))
    time_use.append(time_uses[0])



tariffs = pd.DataFrame(time_use)
print(tariffs)

for i in range(0, len(a)):
    meter = a[i]['meters']
    meters.append(meter)
 
md = {index: value for index, value in enumerate(meters)}
for key, val in a.items():
     
    # iterating over each of the list
    # to fetch all items and print it
    for k, v in val.items():
        # Using f-string here to print
        # the key with each element of a list key
        print(f"{k} : {v}")
         
    # This acts as a separator
    print("--------------------")
 """





    
       
          
   



#print(tariffs)
#tariffs.to_csv('meter12.csv',index=False)
#dataset = pd.json_normalize(data,max_level=2)

#with open('data.json', 'w') as f:
  #  json.dump(data, f)

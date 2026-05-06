
import requests
import json
import pandas as pd

import os

from dotenv import load_dotenv


load_dotenv() 

#djflk
# Build paths inside the project like this: BASE_DIR / 'subdir'.




 # This loads variables from .env into os.environ





def get_all_time_entries():
    DOMAIN = os.getenv("DOMAIN")
    USERNAME = os.getenv("USERNAME")
    API_KEY = os.getenv("API_KEY")

    URL = f"https://commcarehq.org/{DOMAIN}/api/v0.5/form/"


   


    
    headers = {
         "Authorization": f"ApiKey {USERNAME}:{API_KEY}",
         "Content-Type": "application/json"
        }
   
    #http://openrosa.org/formdesigner/8FE19BA3-6F29-4E75-901B-82E1C5563495', 
   
    querystring = {'limit': 1000 }


    page = 1
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # CommCare uses cursor pagination for large datasets
        for case in data['objects']:
            print(case['properties'].get('case_name'))
    else:
        print(f"Error: {response.status_code}", response.text)
        # find out total number of pages
        
        print(response)



    data = res['objects']
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
get_all_time_entries()


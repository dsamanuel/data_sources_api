import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import json
import pandas as pd





def get_all_time_entries():

    url_address = "https://rickandmortyapi.com/api/character"  
 

    # find out total number of pages
    r = requests.get(url=url_address).json()
    total_pages = int(r['info']['pages'])

    # results will be appended to this list
    all_time_entries = []

    # loop through all pages and return JSON object
    for page in range(1, total_pages):

        url = "https://rickandmortyapi.com/api/character?page="+str(page)              
        response = requests.get(url=url).json() 
        result = response['results']    
        all_time_entries.append(result)       
        page += 1

    # prettify JSON
    data = json.dumps(all_time_entries)

    return data

print(get_all_time_entries())
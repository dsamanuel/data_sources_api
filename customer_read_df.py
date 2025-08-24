
from datetime import datetime
from requests.auth import HTTPBasicAuth
import json
import pandas as pd


import numpy as np
import pandas as pd



data = pd.read_json('alldata.json')


for key, value in data.items():
    print(key, value)
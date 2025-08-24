import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

from itertools import chain






df = pd.read_json("mydata.json")
print(df)
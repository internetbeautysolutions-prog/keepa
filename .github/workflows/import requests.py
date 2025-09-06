import requests
import json
import time
import csv
import datetime
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
#from weasyprint import HTML
#from weasyprint import default_url_fetcher, HTML
import os

#Query the Data from the Keepa API and store the response in a JSON Object. 

#Load Sales Ranking Data

url = "https://api.keepa.com/product"
querystring = {9vsudgs2ibd34i12lp9kgj4p7oqfe9f65ot43kgtuekrmer77e9ope39sp6okpua
               "key":"",
               "domain":"1",
               "asin":"B002MSN3QQ"
              }

headers = {
    'cache-control': "no-cache",
    'postman-token': "f3d8335d-684c-6b4d-d76b-6a9d211cc258"
    }

response = requests.request("GET", url, params=querystring)
json_obj = json.loads(response.text)

#Dates and Times from Server
now2 = datetime.datetime.now()
FT = now2.strftime("%Y-%m-%d")
YR = now2.strftime("%Y")
FT3 = now2.strftime("%Y-%m-%d@%H:%M:%S") 
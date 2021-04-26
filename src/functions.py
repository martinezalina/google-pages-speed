from time import sleep
import requests
import json

import pandas as pd
from datetime import datetime

from db_manage import sql_connection, sql_insert_metric
from config import API_Key


baseURL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="

def get_pagespeed(page_URL,API_Key):
    if API_Key !='your-api-key':
        response_url = baseURL+page_URL+'&key='+API_Key
    else:
        response_url = baseURL+page_URL
    response = requests.get(response_url)
    json_data = response.json()
    try:
        lighthouseResult = json_data["lighthouseResult"]
        categories = lighthouseResult["categories"] 
        performance = categories["performance"]
        score = performance["score"]
    except:
        score = None
        print("We couldn't get the metric from this url. Define or check your API_KEY.")
    sleep(2)
    return score


def get_urls_metrics(con):

    print('')
    print('> Init process ok','\n')

    df = pd.read_csv('./data/urls.csv')
    cant = df.shape[0]
    print('> Reading url list. Found',cant,'urls to work with.','\n')

    print('> Getting scores:','\n')
    for row in df.iterrows():
        url = str(row[1].values[0])
        print(url)
        score = get_pagespeed(url,API_Key)
        print('score', score)
        now = datetime.today()
        print('now', now,'\n')
        
        data = (url, score, now)
        sql_insert_metric(con, data)
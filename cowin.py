from datetime import date
import json
import time
import requests
from call import *

with open("data.json","r") as f:
    data = json.load(f)

count = 0

while(1):    

    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=%s&date=%s"%(data['pincode'], date.today().strftime("%d-%m-%Y"))

    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

    res = requests.get(url, headers = header)
    R = res.json()

    data = None
    if 'centers' in R.keys():
        data = R['centers']

    if sum([j['available_capacity_dose1'] for i in data for j in i['sessions'] if j['min_age_limit'] <= 18]) > 0:
        dial()
        count += 1

    if count == 3:
        break

    time.sleep(600)

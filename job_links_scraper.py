import pandas as pd

df = pd.read_csv('analystlinks.csv')

l1 = df.to_dict('records')

with open('full_temp.json', 'w') as f:
    json.dump(l1, f)

from bs4 import BeautifulSoup


import requests
from requests.adapters import HTTPAdapter, Retry


def job_data(data):
    soup = BeautifulSoup(data.text, 'html.parser')
    i_job = {}
    for item in [{"Title":{"name" : "h1" , "tag" : "top-card-layout__title"},
                 "Company":{"name" : "a" , "tag" : "topcard__org-name-link topcard__flavor--black-link"},
                 "Location":{"name" : "span" , "tag" : "topcard__flavor topcard__flavor--bullet"}}]:
        for name, tag in item.items():          
            try:
                i_job[name] = soup.find(tag["name"], class_=tag["tag"]).get_text().replace("\n","").strip()
            except:
                i_job[name] = "Not Found"

    j = soup.find("div", class_="show-more-less-html__markup")
    j_1 = ""
    for j in j:
        if len(j.get_text()) > 0:
            j_1 = j_1 + j.get_text().strip() + " "
    
    i_job["Description"] = j_1
    
    x1 = soup.find("ul", class_="description__job-criteria-list")
    items = ["Seniority level","Employment type","Job function","Industries"]
    
    for i in items:    
        for x in x1:
            if x.name == "li":
                try:
                    a = x.h3.get_text().replace("\n","").strip()
                    if str(a) == i:
                        b = x.span.get_text().replace("\n","").strip()
                        i_job[i] = b
                except:
                    i_job[i] = "Not Found"
                        
        
    return i_job



s = requests.Session()

retries = Retry(total=5,
                backoff_factor=1,
                status_forcelist=[ 429, 500, 502, 503, 504 ])

s.mount('http://', HTTPAdapter(max_retries=retries))

import json
import time
import os

fail_list = []
r_log = []
job = []

def run_script():
    with open('full_temp.json') as f:
        full_temp = json.load(f)
    
    fail_list = []
    r_log = []
    job = []
    
    b_list = full_temp[:20]
    b_len = len(b_list)
    
    while len(full_temp) != 0 and len(b_list) != 0 :
        b_list = full_temp[:20]
        b_len = len(b_list)
        del full_temp[:b_len]
        while len(b_list) != 0:
            
            b = b_list.pop()
            url = b["Link"]
            url = url.split("?position=")[0]
            try: 
                r = s.get(url)
                time.sleep(1)            
                r_log.append(r.status_code)
                if r.status_code == 200 and int(r.headers['Content-Length']) > 15000:
                    j = job_data(r)
                    j["Link"]= url
                    j["Time"] = r.headers["Date"]
                    job.append(j)
                else:
                    fail_list.append(b)    
            except:
                pass
    
    if os.path.exists('fail_list.json') and os.path.getsize('fail_list.json') > 0:
        with open('fail_list.json', 'r') as f:
            try:
                fail_json = json.load(f)
            except json.JSONDecodeError:
                fail_json = []
    else:
        fail_json = []
    

    with open('fail_list.json', 'w') as f:
        fail_json = fail_json + fail_list
        json.dump(fail_json,f)

    
    with open('r_log.json', 'w') as f:
        json.dump(r_log,f)


    if os.path.exists('job_data.json') and os.path.getsize('job_data.json') > 0:
        with open('job_data.json', 'r') as f:
            try:
                job_prev = json.load(f)
            except json.JSONDecodeError:
                job_prev = []
    else:
        job_prev = []
    

    with open('job_data.json', 'w') as f:
        job_prev = job_prev + job
        json.dump(job_prev,f)

    
    

    with open('full_temp.json','w') as f:
        json.dump(full_temp,f)
        
    print("DONE " + str(len(job)))    
    
run_script()

import requests
import json
import time
import pandas as pd

def getPage(p):
    parametres = {
        'specialization': 1,
        'page': p,
        'per_page': 100,
        'period': 1
    }
    req = requests.get('https://api.hh.ru/vacancies', parametres)
    data = req.content.decode()
    req.close()
    return data

result = []
for p in range(20):
    try:
        request = json.loads(getPage(p))
    except Exception as exception:
        raise exception
    for vacancies in request['items']:
        curVacancy = {k: None for k in ('name', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at')}
        curVacancy['name'] = vacancies['name']
        curVacancy['area_name'] = vacancies['area']['name']
        curVacancy['published_at'] = vacancies['published_at']
        if vacancies['salary']:
            curVacancy['salary_from'] = vacancies['salary']['from']
            curVacancy['salary_to'] = vacancies['salary']['to']
            curVacancy['salary_currency'] = vacancies['salary']['currency']
        result.append(curVacancy)
    time.sleep(0.25)
pd.DataFrame.from_records(result).to_csv('desktop/result.csv')

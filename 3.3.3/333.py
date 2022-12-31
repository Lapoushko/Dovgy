import requests
import json
import time
import pandas as pd


def get_page(page):
    params = {
        'specialization': 1,
        'page': page,
        'per_page': 100,
        'period': 1
    }
    request = requests.get('https://api.hh.ru/vacancies', params)
    data = request.content.decode()
    request.close()
    return data


result = []
for page in range(20):
    try:
        request = json.loads(get_page(page))
    except Exception as exception:
        raise exception
    for vacancies in request['items']:
        current_vacancy = {k: None for k in ('name', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at')}
        current_vacancy['name'] = vacancies['name']
        current_vacancy['area_name'] = vacancies['area']['name']
        current_vacancy['published_at'] = vacancies['published_at']
        if vacancies['salary']:
            current_vacancy['salary_from'] = vacancies['salary']['from']
            current_vacancy['salary_to'] = vacancies['salary']['to']
            current_vacancy['salary_currency'] = vacancies['salary']['currency']
        result.append(current_vacancy)
    time.sleep(0.25)
pd.DataFrame.from_records(result).to_csv('desktop/result.csv')

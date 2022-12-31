from stats import *
import pandas as pd
import json

def format_month(month):
    return str(month) if month >= 10 else f'0{month}'

with open('currency_by_years.json', 'r') as file:
    json_file = json.load(file)

df = csv_filter(*csv_reader('vacancies_dif_currencies.csv'))
result = []
for current_vacancy in df:
    if not current_vacancy.salary.salary_from and not current_vacancy.salary.salary_to:
        continue
    salary = 0
    if current_vacancy.salary.salary_from and current_vacancy.salary.salary_to:
        salary = (float(current_vacancy.salary.salary_from) + float(current_vacancy.salary.salary_to)) / 2
    elif current_vacancy.salary.salary_from and not current_vacancy.salary.salary_to:
        salary = float(current_vacancy.salary.salary_from)
    elif not current_vacancy.salary.salary_from and current_vacancy.salary.salary_to:
        salary = float(current_vacancy.salary.salary_to)
    vacancy = current_vacancy.salary.salary_currency
    date_key = f'{current_vacancy.published_at.year}-{format_month(current_vacancy.published_at.month)}'
    if vacancy and vacancy != 'RUR':
        if vacancy not in json_file[date_key].keys():
            continue
        if not json_file[date_key][vacancy]:
            continue
        salary *= json_file[date_key][vacancy]
    result.append({'name': current_vacancy.name, 'salary': salary, 'area_name': current_vacancy.area_name,
                   'published_at': str(current_vacancy.published_at)})
    if len(result) == 100:
        break
pd.DataFrame.from_records(result).to_csv('result.csv')

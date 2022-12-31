import pandas as pd
from pandas import isnull, notnull
from datetime import datetime
import json


def format_month(month):
    return str(month) if month >= 10 else f'0{month}'


with open('currency_by_years.json', 'r') as file:
    json_file = json.load(file)
df: pd.DataFrame = pd.read_csv('vacancies_dif_currencies.csv')[:100]
salary_values = []
headers = ('salary_from', 'salary_to', 'salary_currency', 'published_at')
for i, (salary_from, salary_to, salary_currency, published_at) in enumerate(zip(*[df[index] for index in headers])):
    if isnull(salary_from) and isnull(salary_to):
        df = df.drop(index=i)
        continue
    salary = 0
    if notnull(salary_from) and notnull(salary_to):
        salary = (salary_from + salary_to) / 2
    elif notnull(salary_from) and isnull(salary_to):
        salary = salary_from
    elif isnull(salary_from) and notnull(salary_to):
        salary = salary_to
    published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S+%f')
    date = f'{published_at.year}-{format_month(published_at.month)}'
    if notnull(salary_currency) and salary_currency != 'RUR':
        if salary_currency not in json_file[date].keys():
            df = df.drop(index=i)
            continue
        if not json_file[date][salary_currency]:
            df = df.drop(index=i)
            continue
        salary *= json_file[date][salary_currency]
    salary_values.append(salary)
    if len(salary_values) == 100:
        break

df.insert(2, 'salary', salary_values)
for column in ('salary_from', 'salary_to', 'salary_currency'):
    del df[column]
df.to_csv('result.csv', index=False)

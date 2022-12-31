import pandas as pd
from pandas import isnull, notnull
from datetime import datetime
import json


def monthForm(m):
    return str(m) if m >= 10 else f'0{m}'

with open('currency_by_years.json', 'r') as file:
    json = json.load(file)
value = 100
dataframe: pd.DataFrame = pd.read_csv('vacancies_dif_currencies.csv')[:value]
valOfSalary = []
headers = ('salary_from', 'salary_to', 'salary_currency', 'published_at')
for i, (salary_from, salary_to, salary_currency, published_at) in enumerate(zip(*[dataframe[index] for index in headers])):
    salary = 0
    if isnull(salary_from) and isnull(salary_to):
        dataframe = dataframe.drop(index=i)
        continue
    if notnull(salary_from) and notnull(salary_to):
        salary = (salary_from + salary_to) / 2
    elif isnull(salary_from) and notnull(salary_to):
        salary = salary_to
    elif notnull(salary_from) and isnull(salary_to):
        salary = salary_from
    published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S+%f')
    dateP = f'{published_at.year}-{monthForm(published_at.month)}'
    if notnull(salary_currency) and salary_currency != 'RUR':
        if salary_currency not in json[dateP].keys():
            dataframe = dataframe.drop(index=i)
            continue
        if not json[dateP][salary_currency]:
            dataframe = dataframe.drop(index=i)
            continue
        salary *= json[dateP][salary_currency]
    valOfSalary.append(salary)
    if len(valOfSalary) == value:  break

dataframe.insert(2, 'salary', valOfSalary)
for column in ('salary_from', 'salary_to', 'salary_currency'):  del dataframe[column]
dataframe.to_csv('result.csv', index=False)

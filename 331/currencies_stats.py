from stats import *
import json

data: List[Vacancy] = csv_filer(*csv_reader('vacancies_dif_currencies.csv'))

currencies = {}

for vacancy in data:
    year = vacancy.published_at.year
    currency = vacancy.salary.salary_currency
    
    if not currency:
        continue

    if year not in currencies.keys():
        currencies[year] = {}
    if currency not in currencies[year].keys():
        currencies[year][currency] = 0
    
    currencies[year][currency] += 1

print(json.dumps(currencies, indent=4, ensure_ascii=False))

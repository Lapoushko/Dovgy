from stats import *
import json

data: List[Vacancy] = csv_filer(*csv_reader('vacancies_dif_currencies.csv'))

currens = {}

for vac in data:
    year = vac.published_at.year
    cur = vac.salary.salary_currency
    
    if not cur: continue
    if year not in currens.keys():   currens[year] = {}

    currens[year][cur] += 1

print(json.dumps(currens, indent=4, ensure_ascii=False))

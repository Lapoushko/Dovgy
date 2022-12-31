import pandas as pd

with open('currency_by_years.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('currency_by_years.csv', encoding='utf-8', index=False)
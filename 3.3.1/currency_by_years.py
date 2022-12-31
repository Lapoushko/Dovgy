from urllib.request import urlopen
import xmltodict
import json

currencies = ('USD', 'RUR', 'EUR', 'KZT', 'UAH', 'BYR')

format_month = lambda month: str(month) if month >= 10 else f'0{month}'


def get_value(value: str, nominal: str) -> float:
    return int(nominal) * float(value.replace(',', '.'))


def get_data(month: int, year: int) -> dict:
    month = format_month(month)
    raw_data = \
        xmltodict.parse(urlopen(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{month}/{year}').read())[
            'ValCurs'][
            'Valute']

    return {cur['CharCode']: get_value(cur['Value'], cur['Nominal']) for cur in raw_data if
            cur['CharCode'] in currencies}


result = {}

for year in range(2003, 2023):
    for month in range(1, 13):
        result[f'{year}-{format_month(month)}'] = get_data(month, year)

with open('result.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(result, indent=4, ensure_ascii=False))

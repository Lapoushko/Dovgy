from urllib.request import urlopen
import xmltodict
import json

curr = ('USD', 'RUR', 'EUR', 'KZT', 'UAH', 'BYR')

monthForm = lambda month: str(month) if month >= 10 else f'0{month}'

def getD(m: int, y: int) -> dict:
    m = monthForm(m)
    dataRaw = \
        xmltodict.parse(urlopen(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{m}/{y}').read())[
            'ValCurs'][
            'Valute']

    return {cur['CharCode']: get_value(cur['Value'], cur['Nominal']) for cur in dataRaw if
            cur['CharCode'] in curr}

def get_value(v: str, n: str) -> float:
    return int(n) * float(v.replace(',', '.'))

result = {}

for year in range(2003, 2023):
    for month in range(1, 13):
        result[f'{year}-{monthForm(month)}'] = getD(month, year)

with open('result.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(result, indent=4, ensure_ascii=False))

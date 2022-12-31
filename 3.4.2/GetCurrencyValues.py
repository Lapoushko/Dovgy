import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class GetCurrencyValues:
    def __init__(self, currency):
        self.currency = currency

    def get_currencies(self, date):
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{date}d=1"
        res = session.get(url)
        cur_df = pd.read_xml(res.text)
        values = []
        for currency in self.currency:
            if currency in cur_df["CharCode"].values:
                values.append(round(float(cur_df.loc[cur_df["CharCode"] == currency]["Value"].values[0].replace(',', "."))
                                     / float(cur_df.loc[cur_df["CharCode"] == currency]["Nominal"]), 4))
            else:
                values.append(0)
        return [date] + values

    def get_date(self, first, second):
        result = []
        for year in range(int(first[:4]), int(second[:4]) + 1):
            num = 1
            if str(year) == first[:4]:
                num = int(first[-2:])
            for month in range(num, 13):
                if len(str(month)) == 2:
                    result.append(f"{month}/{year}")
                else:
                    result.append(f"0{month}/{year}")
                if str(year) == second[:4] and (str(month) == second[-2:] or f"0{month}" == second[-2:]):
                    break
        return result

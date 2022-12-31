import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class GetCurrencyValues:
    def __init__(self, cur):
        self.currency = cur

    def getDate(self, first_date, second_date):
        res = []
        for year in range(int(first_date[:4]), int(second_date[:4]) + 1):
            number = 1
            if str(year) == first_date[:4]:
                number = int(first_date[-2:])
            for month in range(number, 13):
                if len(str(month)) == 2:
                    res.append(f"{month}/{year}")
                else:
                    res.append(f"0{month}/{year}")
                if str(year) == second_date[:4] and (str(month) == second_date[-2:] or f"0{month}" == second_date[-2:]):
                    break
        return res

    def getCurs(self, date):
        sess = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        sess.mount('http://', adapter)
        sess.mount('https://', adapter)
        url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{date}d=1"
        res = sess.get(url)
        curDataFrame = pd.read_xml(res.text)
        vals = []
        for cur in self.currency:
            if cur in curDataFrame["CharCode"].values:
                vals.append(round(float(curDataFrame.loc[curDataFrame["CharCode"] == cur]["Value"].values[0].replace(',', ".")) / float(curDataFrame.loc[curDataFrame["CharCode"] == cur]["Nominal"]), 4))
            else:
                vals.append(0)
        return [date] + vals


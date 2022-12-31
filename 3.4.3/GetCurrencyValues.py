import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class GetCurrencyValues:
    def __init__(self, cur):
        self.currency = cur
    def getDate(self, first, second):
        res = []
        for y in range(int(first[:4]), int(second[:4]) + 1):
            number = 1
            if str(y) == first[:4]:
                number = int(first[-2:])
            for month in range(number, 13):
                if len(str(month)) == 2:
                    res.append(f"{month}/{y}")
                else:
                    res.append(f"0{month}/{y}")
                if str(y) == second[:4] and (str(month) == second[-2:] or f"0{month}" == second[-2:]):
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
        values = []
        for cur in self.currency:
            if cur in curDataFrame["CharCode"].values:
                values.append(round(float(curDataFrame.loc[curDataFrame["CharCode"] == cur]["Value"].values[0].replace(',', ".")) / float(curDataFrame.loc[curDataFrame["CharCode"] == cur]["Nominal"]), 4))
            else:
                values.append(0)
        return [date] + values
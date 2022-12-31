import pandas as pd


class CurrencyFormatter:
    def __init__(self, date, salaryCur):
        self.date = date
        self.salary_currency = salaryCur

    def getCur(self):
        if self.salary_currency == "RUR":
            return 1
        currs = pd.read_csv("valutes.csv")
        cur = currs.loc[currs["date"] == self.date]
        if cur.__contains__(self.salary_currency):
            return float(cur[self.salary_currency])
        return 0

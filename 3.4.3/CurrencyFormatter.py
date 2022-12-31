import pandas as pd


class CurrencyFormatter:
    def __init__(self, date, salaryCur):
        self.date = date
        self.salary_currency = salaryCur

    def getCurrency(self):
        if self.salary_currency == "RUR":
            return 1
        curs = pd.read_csv("valutes.csv")
        cur = curs.loc[curs["date"] == self.date]
        if cur.__contains__(self.salary_currency):
            return float(cur[self.salary_currency])
        return 0

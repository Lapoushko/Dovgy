import pandas as pd


class CurrencyFormatter:
    def __init__(self, date, salary_currency):
        self.date = date
        self.salary_currency = salary_currency

    def get_currency(self):
        if self.salary_currency == "RUR":
            return 1
        currencies = pd.read_csv("valutes.csv")
        currency = currencies.loc[currencies["date"] == self.date]
        if currency.__contains__(self.salary_currency):
            return float(currency[self.salary_currency])
        return 0

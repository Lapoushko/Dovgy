from CurrencyFormatter import CurrencyFormatter


class Salary:
    # Класс для представления зарплат

    def __init__(self, fromSalary, toSalary, salaryCur, published):
        self.salary_from = self.checkStr(fromSalary)
        self.salary_to = self.checkStr(toSalary)
        self.salary_currency = salaryCur
        self.published_at = published
        self.month_year = f"{self.published_at[5:7]}/{self.published_at[:4]}"

    def checkStr(self, v):
        if v == "" and type(v) == str:
            return 0
        return float(v)

    def get_average_salary(self):
        return round(((self.salary_from + self.salary_to) * CurrencyFormatter(self.month_year,self.salary_currency).getCurr()) / 2, 4)

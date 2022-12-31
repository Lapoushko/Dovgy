from CurrencyFormatter import CurrencyFormatter


class Salary:
    # Класс для представления зарплат
    def __init__(self, salaryFrom: str or int or float, salaryTo: str or int or float, salaryCur: str,
                 published_at: str):
        self.salary_from = self.check_value(salaryFrom)
        self.salary_to = self.check_value(salaryTo)
        self.salary_currency = salaryCur
        self.published_at = published_at
        self.month_year = f"{self.published_at[5:7]}/{self.published_at[:4]}"

    def get_average_salary(self):
        return round(((self.salary_from + self.salary_to) * CurrencyFormatter(self.month_year,
                                                                              self.salary_currency).getCur()) / 2, 4)

    def check_value(self, v):
        if type(v) == str and v == "":  return 0
        return float(v)



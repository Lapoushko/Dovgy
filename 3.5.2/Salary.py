from CurrencyFormatter import CurrencyFormatter


class Salary:
    """
    Класс для представления зарплат
    """
    def __init__(self, salary_from: str or int or float, salary_to: str or int or float, salary_currency: str,
                 published_at: str):
        self.salary_from = self.check_value(salary_from)
        self.salary_to = self.check_value(salary_to)
        self.salary_currency = salary_currency
        self.published_at = published_at
        self.month_year = f"{self.published_at[5:7]}/{self.published_at[:4]}"

    def check_value(self, value):
        if type(value) == str and value == "":
            return 0
        return float(value)

    def get_average_salary(self):
        return round(((self.salary_from + self.salary_to) * CurrencyFormatter(self.month_year, self.salary_currency).get_currency()) / 2, 4)

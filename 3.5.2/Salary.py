from CurrencyFormatter import CurrencyFormatter


class Salary:

    # Класс для представления зарплат

    def check_value(self, v):
        if type(v) == str and v == "":
            return 0
        return float(v)

    def __init__(self, formSalary: str or int or float, toSalary: str or int or float, curSalary: str,
                 published: str):
        self.salary_from = self.check_value(formSalary)
        self.salary_to = self.check_value(toSalary)
        self.salary_currency = curSalary
        self.published_at = published
        self.month_year = f"{self.published_at[5:7]}/{self.published_at[:4]}"



    def get_average_salary(self):
        return round(((self.salary_from + self.salary_to) * CurrencyFormatter(self.month_year, self.salary_currency).getCur()) / 2, 4)

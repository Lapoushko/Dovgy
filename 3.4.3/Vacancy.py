from Salary import Salary


class Vacancy:
    """
    Класс для представления вакансий
    """

    def __init__(self, vacancy):
        self.name = vacancy["name"]
        self.salary = Salary(salary_from=vacancy["salary_from"],
                             salary_to=vacancy["salary_to"],
                             salary_currency=vacancy["salary_currency"],
                             published_at=vacancy["published_at"])
        self.area_name = vacancy["area_name"]
        self.published_at = vacancy["published_at"]
        self.year = self.published_at[:4]

    def get_array_vacancy(self):
        return [self.name, self.salary.get_average_salary(), self.area_name, self.published_at]

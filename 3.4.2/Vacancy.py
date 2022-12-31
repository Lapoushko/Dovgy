
from Salary import Salary


class Vacancy:
    # Класс для представления вакансий

    def getListVac(self):
        return [self.name, self.salary.get_average_salary(), self.area_name, self.published_at]

    def __init__(self, vac):
        self.name = vac["name"]
        self.salary = Salary(salary_from=vac["salary_from"], salary_to=vac["salary_to"],
                             salary_currency=vac["salary_currency"], published_at=vac["published_at"])
        self.area_name = vac["area_name"]
        self.published_at = vac["published_at"]
        self.year = self.published_at[:4]
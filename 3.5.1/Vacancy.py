from Salary import Salary


class Vacancy:
    # Класс для представления вакансий

    def __init__(self, vac):
        self.name = vac["name"]
        self.salary = Salary(salaryFrom=vac["salary_from"],
                             salaryTo=vac["salary_to"],
                             salaryCur=vac["salary_currency"],
                             published_at=vac["published_at"])
        self.area_name = vac["area_name"]
        self.published_at = vac["published_at"]
        self.year = self.published_at[:4]

    def getListVac(self):
        return [self.name, self.salary.get_average_salary(), self.area_name, self.published_at]

from DataSet import DataSet
from YearSalary import YearSalary
from Salary import Salary

class Stat:
    """
    Класс для обработки, иницилизации данных  представления статистики
    """
    def __init__(self, profession):
        self.profession = profession

    def data_formatter(self, file_name):
        data = DataSet(file_name).vacancies_objects
        data_profession = [d for d in data if self.profession in d.name]
        year_salary = self.convert_to_param_salary(data)
        professions_year_salary = self.add_missing_years(self.convert_to_param_salary(data_profession), year_salary)
        year_salary, year_vacancy = self.convert_from_param_salary_to_dict(year_salary)
        professions_year_salary, professions_year_vacancies = self.convert_from_param_salary_to_dict(professions_year_salary)
        return year_salary, year_vacancy, professions_year_salary, professions_year_vacancies

    def convert_to_param_salary(self, vacancies):
        param_salary = {}
        for vacancy in vacancies:
            if not param_salary.__contains__(vacancy.year):
                param_salary[vacancy.year] = YearSalary(vacancy.year, vacancy.salary)
            else:
                param_salary[vacancy.year] = param_salary[vacancy.year].add_salary(vacancy.salary)
        return [param_salary[d] for d in param_salary]

    def convert_from_param_salary_to_dict(self, param_salary):
        return {x: y for x, y in zip([int(r.param) for r in param_salary],
                                     [0 if v.count_vacancies == 0 else int(v.salary / v.count_vacancies) for v in param_salary])},\
               {x: y for x, y in zip([int(r.param) for r in param_salary], [v.count_vacancies for v in param_salary])}

    def add_missing_years(self, param_salary, year_salary):
        years = [i.param for i in year_salary]
        s_years = [el.param for el in param_salary]
        for y in years:
            if y not in s_years:
                param_salary.insert(int(y) - int(years[0]), YearSalary(y, Salary("0", "0", "RUR", "2003-10-07T00:00:00+0400")))
                param_salary[int(y) - int(years[0])].count_vacancies = 0
        return param_salary

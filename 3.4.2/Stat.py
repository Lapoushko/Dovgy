from YearSalary import YearSalary
from Salary import Salary
from DataSet import DataSet


class Stat:

    # Класс для обработки, иницилизации данных  представления статистики


    def __init__(self, profes):
        self.profession = profes

    def convertParamSalary(self, vacs):
        salary = {}
        for vac in vacs:
            if not (salary.__contains__(vac.year)):
                salary[vac.year] = YearSalary(vac.year, vac.salary)
            else:
                salary[vac.year] = salary[vac.year].addNewSalary(vac.salary)
        return [salary[d] for d in salary]

    def procData(self, file_name):
        data = DataSet(file_name).vacsObj
        dataProf = [d for d in data if self.profession in d.name]
        salaryYear = self.convertParamSalary(data)
        salaryYearProf = self.addMissing(self.convertParamSalary(dataProf), salaryYear)
        salaryYear, yearVac = self.convertSalaryDictionary(salaryYear)
        salaryYearProf, yearVacProfes = self.convertSalaryDictionary(salaryYearProf)
        return salaryYear, yearVac, salaryYearProf, yearVacProfes



    def addMissing(self, salary, salaryYear):
        years = [i.param for i in salaryYear]
        s_years = [el.param for el in salary]
        for y in years:
            if y not in s_years:
                salary.insert(int(y) - int(years[0]), YearSalary(y, Salary("0", "0", "RUR", "2003-10-07T00:00:00+0400")))
                salary[int(y) - int(years[0])].count_vacancies = 0
        return salary

    def convertSalaryDictionary(self, salary):
        return {x: y for x, y in zip([int(r.param) for r in salary],
                                     [0 if v.count_vacancies == 0 else int(v.salary / v.count_vacancies) for v in
                                      salary])}, \
               {x: y for x, y in zip([int(r.param) for r in salary], [v.count_vacancies for v in salary])}



from DataSet import DataSet
from YearSalary import YearSalary
from Salary import Salary

class Stat:
    # Класс для обработки, иницилизации данных  представления статистики
    def __init__(self, profes):
        self.profession = profes

    def formatter(self, nameFile):
        arr = DataSet(nameFile).vacsObj
        profesArray = [d for d in arr if self.profession in d.name]
        salaryYear = self.convertParamSalary(arr)
        salaryYearProf = self.addMissing(self.convertParamSalary(profesArray), salaryYear)
        salaryYear, vacYear = self.convertParamSalaryDictionary(salaryYear)
        salaryYearProf, vacYearProf = self.convertParamSalaryDictionary(salaryYearProf)
        return salaryYear, vacYear, salaryYearProf, vacYearProf

    def convertParamSalary(self, vacs):
        salaryParam = {}
        for vac in vacs:
            if not salaryParam.__contains__(vac.year):
                salaryParam[vac.year] = YearSalary(vac.year, vac.salary)
            else:
                salaryParam[vac.year] = salaryParam[vac.year].addSalary(vac.salary)
        return [salaryParam[d] for d in salaryParam]



    def addMissing(self, salaryParam, salaryYEar):
        years = [i.param for i in salaryYEar]
        s_years = [el.param for el in salaryParam]
        for y in years:
            if y not in s_years:
                salaryParam.insert(int(y) - int(years[0]), YearSalary(y, Salary("0", "0", "RUR", "2003-10-07T00:00:00+0400")))
                salaryParam[int(y) - int(years[0])].count_vacancies = 0
        return salaryParam

    def convertParamSalaryDictionary(self, salaryParam):
        return {x: y for x, y in zip([int(r.param) for r in salaryParam],
                                     [0 if v.count_vacancies == 0 else int(v.salary / v.count_vacancies) for v in
                                      salaryParam])}, \
            {x: y for x, y in zip([int(r.param) for r in salaryParam], [v.count_vacancies for v in salaryParam])}

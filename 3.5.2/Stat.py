from DataSet import DataSet
from YearSalary import YearSalary
from Salary import Salary

class Stat:
    # Класс для обработки, иницилизации данных  представления статистики

    def __init__(self, profes):
        self.profession = profes

    def formatter(self, nameFile):
        data = DataSet(nameFile).vacsObj
        profes = [d for d in data if self.profession in d.name]
        salaryYear = self.convertingParamSalary(data)
        salaryYearProf = self.addMissing(self.convertingParamSalary(profes), salaryYear)
        salaryYear, vacYear = self.convertingSalaryDictionary(salaryYear)
        salaryYearProf, vacsYearProf = self.convertingSalaryDictionary(salaryYearProf)
        return salaryYear, vacYear, salaryYearProf, vacsYearProf

    def addMissing(self, salaryCrit, salaryYear):
        years = [i.param for i in salaryYear]
        yearsS = [el.param for el in salaryCrit]
        for y in years:
            if y not in yearsS:
                salaryCrit.insert(int(y) - int(years[0]), YearSalary(y, Salary("0", "0", "RUR", "2003-10-07T00:00:00+0400")))
                salaryCrit[int(y) - int(years[0])].count_vacancies = 0
        return salaryCrit

    def convertingParamSalary(self, vacs):
        salaryCrit = {}
        for vac in vacs:
            if not salaryCrit.__contains__(vac.year):
                salaryCrit[vac.year] = YearSalary(vac.year, vac.salary)
            else:
                salaryCrit[vac.year] = salaryCrit[vac.year].addNewSalary(vac.salary)
        return [salaryCrit[d] for d in salaryCrit]

    def convertingSalaryDictionary(self, salaryCrit):
        return {x: y for x, y in zip([int(r.param) for r in salaryCrit],
                                     [0 if v.count_vacancies == 0 else int(v.salary / v.count_vacancies) for v in salaryCrit])},\
               {x: y for x, y in zip([int(r.param) for r in salaryCrit], [v.count_vacancies for v in salaryCrit])}


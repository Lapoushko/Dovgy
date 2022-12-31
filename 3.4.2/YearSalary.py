class YearSalary:

    # Класс для представления параметра и связанной с ним зарплаты


    def addNewSalary(self, new):
        self.count_vacancies += 1
        self.salary = self.salary + new.get_average_salary()
        return self

    def __init__(self, param, salary):
        self.param = param
        self.salary = salary.get_average_salary()
        self.count_vacancies = 1



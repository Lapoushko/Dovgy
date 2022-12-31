

class YearSalary:

    # Класс для представления параметра и связанной с ним зарплаты


    def addNewSalary(self, salary):
        self.count_vacancies += 1
        self.salary = self.salary + salary.get_average_salary()
        return self
    def __init__(self, crit, salary):
        self.param = crit
        self.salary = salary.get_average_salary()
        self.count_vacancies = 1


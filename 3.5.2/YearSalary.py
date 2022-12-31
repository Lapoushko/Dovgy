

class YearSalary:
    """
    Класс для представления параметра и связанной с ним зарплаты
    """

    def __init__(self, param, salary):
        self.param = param
        self.salary = salary.get_average_salary()
        self.count_vacancies = 1

    def add_salary(self, new_salary):
        self.count_vacancies += 1
        self.salary = self.salary + new_salary.get_average_salary()
        return self

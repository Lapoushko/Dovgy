import os
import numpy as np
from matplotlib import pyplot as plt


class MakeGraph:
    """Класс для создания графиков с помощью библиотеки matpolib"""
    def __init__(self, profession, years, average_salary, average_salary_profession, count_vacancies_by_year,
                 count_vacancies_by_year_prof, file_name):
        if not isinstance(file_name, str):
            raise TypeError('')
        if os.path.basename(file_name).split('.')[1] != "png":
            raise TypeError('')
        if os.path.exists(file_name):
            raise FileExistsError("")
        self.years = years
        self.average_salary = average_salary
        self.average_salary_profession = average_salary_profession
        self.count_vacancies_by_year = count_vacancies_by_year
        self.count_vacancies_by_year_prof = count_vacancies_by_year_prof
        self.profession = profession
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
        self.grouped_graph(ax1, "Уровень зарплат по годам", self.average_salary, self.years,
                           self.average_salary_profession, 'средняя з/п', f'з/п {self.profession}')
        self.grouped_graph(ax2, 'Количество вакансий по годам', self.count_vacancies_by_year, self.years,
                           self.count_vacancies_by_year_prof, 'Количество вакансий', f'Количество вакансий {self.profession}')
        plt.tight_layout()
        fig.savefig(file_name)

    def grouped_graph(self, ax, title, values_x, values_y, values_x2, label_x, label_x2):
        ax.grid(axis='y')
        x = np.arange(len(values_y))
        width = 0.4
        ax.bar(x - width / 2, values_x, width, label=label_x)
        ax.bar(x + width / 2, values_x2, width, label=label_x2)
        ax.set_xticks(x, values_y, rotation=90)
        ax.tick_params(axis="both", labelsize=16)
        ax.set_title(title, fontweight='normal', fontsize=20)
        ax.legend(loc="upper left", fontsize=14)

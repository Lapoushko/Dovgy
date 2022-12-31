import numpy as np
from matplotlib import pyplot as plt

class MakeGraph:
    # Класс для создания графиков с помощью библиотеки matpolib

    def __init__(self, profes, years, avgSalary, avgSalaryProf, countVacsYear,
                 countVacsYearProf, nameFile):
        self.years = years
        self.avgSalary = avgSalary
        self.avgSalaryProf = avgSalaryProf
        self.countVacsYear = countVacsYear
        self.countVacsYearProf = countVacsYearProf
        self.profession = profes
        figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
        self.grouped_graph(ax1, "Уровень зарплат по годам", self.avgSalary, self.years,
                           self.avgSalaryProf, 'средняя з/п', f'з/п {self.profession}')
        self.grouped_graph(ax2, 'Количество вакансий по годам', self.countVacsYear, self.years,
                           self.countVacsYearProf, 'Количество вакансий',
                               f'Количество вакансий {self.profession}')
        plt.tight_layout()
        figure.savefig(nameFile)

    def grouped_graph(self, ax, title, valuesX1, valuesY1, valuesX2, labelX1, labelX2):
        ax.grid(axis='y')
        x = np.arange(len(valuesY1))
        ax.bar(x - 0.4 / 2, valuesX1, 0.4, label=labelX1)
        ax.bar(x + 0.4 / 2, valuesX2, 0.4, label=labelX2)
        ax.set_xticks(x, valuesY1, rotation=90)
        ax.tick_params(axis="both", labelsize=16)
        ax.set_title(title, fontweight='normal', fontsize=20)
        ax.legend(loc="upper left", fontsize=14)

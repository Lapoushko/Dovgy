import re
import csv
from Vacancy import Vacancy


class DataSet:
    # Класс для представления набора вакансий
    def __init__(self, nameFile: str):
        self.nameFile = nameFile
        self.vacsObj = self.reader()

    def formatter(self, hds, vacs):
        # Отбирает правильно заполненные вакансии и конвертирует в класс Vacancy
        res = []
        for vac in vacs:
            vac = [" ".join(re.sub("<.*?>", "", value).replace('\n', '; ').split()) for value in vac]
            res.append(Vacancy({x: y for x, y in zip([r for r in hds], [v for v in vac])}))
        return res
    def reader(self):
        with open(self.nameFile, encoding='utf-8-sig') as file:
            fileReader = csv.reader(file)
            lines = [row for row in fileReader]
            hds, vacs = lines[0], lines[1:]
        return self.formatter(hds, vacs)



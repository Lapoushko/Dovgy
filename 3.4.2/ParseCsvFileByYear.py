import csv
import os
import re
import pandas as pd


class ParseCsvFileByYear:
    # Класс для раделения набора вакансий по годам

    def __init__(self, nameFile, dir):
        self.nameFile = nameFile
        self.dir = dir
        self.hds, self.vacs = self.reader()
        self.formatter(self.hds, self.vacs)



    def formatter(self, hds, vacs):
        # Обрабатывает полученный набор вакансий и загаловков
        curYear = "0"
        self.firstVac = ""
        os.mkdir(self.dir)
        vacsByYEar = []
        for vac in vacs:
            if (len(vac) == len(hds)) and (
                    (all([v != "" for v in vac])) or (vac[2] != "" and vac[1] == "") or (
                    vac[1] != "" and vac[2] == "")):
                vac = [" ".join(re.sub("<.*?>", "", v).replace('\n', '; ').split()) for v in vac]
                if len(self.firstVac) == 0:
                    self.firstVac = vac
                arrayVacs = [v for v in vac]
                if vac[-1][:4] != curYear:
                    if len(vacsByYEar) != 0:
                        self.__csv_writer(hds, vacsByYEar, curYear)
                        vacsByYEar.clear()
                    curYear = vac[-1][:4]
                vacsByYEar.append(arrayVacs)
                self.lastVac = vac
        self.__csv_writer(hds, vacsByYEar, curYear)

    def reader(self):
        # Читает из csv файла вакансии и возвращает в виде списка загаловков и набора вакансий
        with open(self.nameFile, encoding='utf-8-sig') as file:
            file = csv.reader(file)
            lines = [row for row in file]
        return lines[0], lines[1:]

    def __csv_writer(self, hds, vacs, curYear):
        # Записывает данные в csv-файл
        name = os.path.splitext(self.nameFile)
        vacs = pd.DataFrame(vacs, columns=hds)
        vacs.to_csv(f'{self.dir}/{name[0]}_{curYear}.csv', index=False)

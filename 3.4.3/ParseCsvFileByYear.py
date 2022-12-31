import csv
import os
import re
import pandas as pd


class ParseCsvFileByYear:
    """
    Класс для раделения набора вакансий по годам
    """

    def __init__(self, nameFile, dir):
        self.nameFile = nameFile
        self.dir = dir
        self.hds, self.vacs = self.reader()
        self.formater(self.hds, self.vacs)

    def reader(self):
        with open(self.nameFile, encoding='utf-8-sig') as f:
            fileReader = csv.reader(f)
            lines = [row for row in fileReader]
        return lines[0], lines[1:]

    def formater(self, hds, vacs):
        curYear = "0"
        self.firstVac = ""
        os.mkdir(self.dir)
        vacsCurYear = []
        for vac in vacs:
            if (len(vac) == len(hds)) and (
                    (all([v != "" for v in vac])) or (vac[1] == "" and vac[2] != "") or (
                    vac[1] != "" and vac[2] == "")):
                vac = [" ".join(re.sub("<.*?>", "", value).replace('\n', '; ').split()) for value in vac]
                if len(self.firstVac) == 0:
                    self.firstVac = vac
                listVac = [v for v in vac]
                if vac[-1][:4] != curYear:
                    if len(vacsCurYear) != 0:
                        self.writer(hds, vacsCurYear, curYear)
                        vacsCurYear.clear()
                    curYear = vac[-1][:4]
                vacsCurYear.append(listVac)
                self.lastVac = vac
        self.writer(hds, vacsCurYear, curYear)

    def writer(self, hds, vacs, curYear):
        name = os.path.splitext(self.nameFile)
        vacs = pd.DataFrame(vacs, columns=hds)
        vacs.to_csv(f'{self.dir}/{name[0]}_{curYear}.csv', index=False)

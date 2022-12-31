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

    def reader(self):
        with open(self.nameFile, encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines[0], lines[1:]

    def writer(self, hds, vacs, curYear):
        name = os.path.splitext(self.nameFile)
        vacs = pd.DataFrame(vacs, columns=hds)
        vacs.to_csv(f'{self.dir}/{name[0]}_{curYear}.csv', index=False)

    def formatter(self, hds, vacs):
        curYear = "0"
        self.firstVac = ""
        os.mkdir(self.dir)
        vacCurYEar = []
        for vac in vacs:
            if (len(vac) == len(hds)) and (
                    (all([v != "" for v in vac])) or (vac[1] == "" and vac[2] != "") or (
                    vac[1] != "" and vac[2] == "")):
                vac = [" ".join(re.sub("<.*?>", "", value).replace('\n', '; ').split()) for value in vac]
                if len(self.firstVac) == 0:
                    self.firstVac = vac
                vacArray = [v for v in vac]
                if vac[-1][:4] != curYear:
                    if len(vacCurYEar) != 0:
                        self.writer(hds, vacCurYEar, curYear)
                        vacCurYEar.clear()
                    curYear = vac[-1][:4]
                vacCurYEar.append(vacArray)
                self.lastVac = vac
        self.writer(hds, vacCurYEar, curYear)



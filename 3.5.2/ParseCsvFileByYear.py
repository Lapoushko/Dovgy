import csv
import os
import re
import pandas as pd


class ParseCsvFileByYear:
    """
    Класс для раделения набора вакансий по годам
    """

    def __init__(self, file_name, directory):
        self.file_name = file_name
        self.dir_name = directory
        self.headlines, self.vacancies = self.csv_reader()
        self.csv_formatter(self.headlines, self.vacancies)

    def csv_reader(self):
        with open(self.file_name, encoding='utf-8-sig') as file:
            file_reader = csv.reader(file)
            lines = [row for row in file_reader]
        return lines[0], lines[1:]

    def csv_formatter(self, headlines, vacancies):
        cur_year = "0"
        self.first_vacancy = ""
        os.mkdir(self.dir_name)
        vacancies_cur_year = []
        for vacancy in vacancies:
            if (len(vacancy) == len(headlines)) and (
                    (all([v != "" for v in vacancy])) or (vacancy[1] == "" and vacancy[2] != "") or (
                    vacancy[1] != "" and vacancy[2] == "")):
                vacancy = [" ".join(re.sub("<.*?>", "", value).replace('\n', '; ').split()) for value in vacancy]
                if len(self.first_vacancy) == 0:
                    self.first_vacancy = vacancy
                vacancy_list = [v for v in vacancy]
                if vacancy[-1][:4] != cur_year:
                    if len(vacancies_cur_year) != 0:
                        self.csv_writer(headlines, vacancies_cur_year, cur_year)
                        vacancies_cur_year.clear()
                    cur_year = vacancy[-1][:4]
                vacancies_cur_year.append(vacancy_list)
                self.last_vacancy = vacancy
        self.csv_writer(headlines, vacancies_cur_year, cur_year)

    def csv_writer(self, headlines, vacancies, cur_year):
        name = os.path.splitext(self.file_name)
        vacancies = pd.DataFrame(vacancies, columns=headlines)
        vacancies.to_csv(f'{self.dir_name}/{name[0]}_{cur_year}.csv', index=False)

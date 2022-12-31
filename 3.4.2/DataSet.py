import re
import csv
from Vacancy import Vacancy


class DataSet:
    """Класс для представления набора вакансий"""

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.vacancies_objects = self.csv_reader()

    def csv_reader(self):
        with open(self.file_name, encoding='utf-8-sig') as file:
            file_reader = csv.reader(file)
            lines = [row for row in file_reader]
            headlines, vacancies = lines[0], lines[1:]
        return self.vacancies_formatter(headlines, vacancies)

    def vacancies_formatter(self, headlines, vacancies):
        """
        Отбирает правильно заполненные вакансии и конвертирует в класс Vacancy
        """
        result = []
        for vacancy in vacancies:
            vacancy = [" ".join(re.sub("<.*?>", "", value).replace('\n', '; ').split()) for value in vacancy]
            result.append(Vacancy({x: y for x, y in zip([r for r in headlines], [v for v in vacancy])}))
        return result

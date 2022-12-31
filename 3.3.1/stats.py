import csv
import re
from typing import List
from datetime import datetime


class DataSet:
    def __init__(self, file_name, vacancies_objects):
        self.file_name = file_name
        self.vacancies_objects = vacancies_objects


class Vacancy:
    def __init__(self, name, salary, area_name, published_at):
        self.name = name
        self.salary: Salary = salary
        self.area_name = area_name
        self.published_at: datetime = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S+%f')


class Salary:
    def __init__(self, salary_from, salary_to, salary_currency):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency


def format_value(dict_object: dict, key: str, value: str):
    value = re.sub('\r', '', value)
    value = re.sub(r'<[^>]+>', '', value, flags=re.S)
    value = '\n'.join(map(lambda i: i.strip(), value.split('\n'))) if '\n' in value else ' '.join(value.strip().split())
    dict_object[key] = value


def csv_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8', newline='') as file:
        return re.sub('\n|\r|\ufeff', '', file.readline()).split(','), list(csv.reader(file))


def csv_filer(titles: list, data: list):
    vacancies_objects = []

    for vacancy_data in data:
        vacancy = {key: None for key in ('name', 'area_name', 'published_at')}
        salary = {key: None for key in ('salary_from', 'salary_to', 'salary_currency')}
        for key, value in zip(titles, vacancy_data):
            format_value(salary if 'salary' in key else vacancy, key, value)

        vacancy['salary'] = Salary(**salary)
        vacancies_objects.append(Vacancy(**vacancy))

    return vacancies_objects

import csv
import re
from datetime import datetime


class DataSet:
    def __init__(self, nameFile, vacs):
        self.file_name = nameFile
        self.vacancies_objects = vacs


class Vacancy:
    def __init__(self, name, salary, area, published):
        self.name = name
        self.salary: Salary = salary
        self.area_name = area
        self.published_at: datetime = datetime.strptime(published, '%Y-%m-%dT%H:%M:%S+%f')


class Salary:
    def __init__(self, salary_from, salary_to, salary_currency):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency

def csv_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8', newline='') as file:
        return re.sub('\n|\r|\ufeff', '', file.readline()).split(','), list(csv.reader(file))

def format_value(dict_object: dict, key: str, val: str):
    val = re.sub('\r', '', val)
    val = re.sub(r'<[^>]+>', '', val, flags=re.S)
    val = '\n'.join(map(lambda i: i.strip(), val.split('\n'))) if '\n' in val else ' '.join(val.strip().split())
    dict_object[key] = val

def csv_filer(titles: list, data: list):
    vacsArrays = []

    for vacData in data:
        vac = {key: None for key in ('name', 'area_name', 'published_at')}
        salary = {key: None for key in ('salary_from', 'salary_to', 'salary_currency')}
        for key, value in zip(titles, vacData):
            format_value(salary if 'salary' in key else vac, key, value)

        vac['salary'] = Salary(**salary)
        vacsArrays.append(Vacancy(**vac))

    return vacsArrays
import re
import prettytable
from prettytable import PrettyTable
import csv


class DataSet:
    translate_dict = {"noExperience": "Нет опыта", "between1And3": "От 1 года до 3 лет",
                       "between3And6": "От 3 до 6 лет", "moreThan6": "Более 6 лет", "AZN": "Манаты",
                       "BYR": "Белорусские рубли", "EUR": "Евро", "GEL": "Грузинский лари",
                       "KGS": "Киргизский сом", "KZT": "Тенге", "RUR": "Рубли", "UAH": "Гривны",
                       "USD": "Доллары", "UZS": "Узбекский сум", "True": "Да", "False": "Нет", "FALSE": "Нет",
                       "TRUE": "Да"}

    def __init__(self):
        self.file_name = file_name
        headlines, vacancies = self.csv_reader()
        dict_list = self.csv_filter(vacancies, headlines)
        self.vacancies_fields = [Vacancy(current_dict) for current_dict in dict_list]

    def csv_reader(self):
        headlines_list = vacancies_list = []
        length = count = 0
        flag = True
        with open(file_name, encoding="utf-8-sig") as File:
            reader_obj = csv.reader(File)
            for current_row in reader_obj:
                count += 1
                if flag:
                    flag = False
                    headlines_list = current_row
                    length = len(current_row)
                else:
                    flag_to_continue = False
                    if length != len(current_row):
                        flag_to_continue = True
                    for word in current_row:
                        if word == "":
                            flag_to_continue = True
                    if flag_to_continue:
                        continue
                    vacancies_list.append(current_row)
        if count == 1:
            print("Нет данных")
            exit()
        elif count == 0:
            print("Пустой файл")
            exit()
        else:
            return headlines_list, vacancies_list

    def csv_filter(self, reader_obj, headers):
        dicts_list = []
        for current_vacancy in reader_obj:
            current_dict = {}
            for i in range(len(headers)):
                current_dict[headers[i]] = self.string_formatter(current_vacancy[i])
            dicts_list.append(current_dict)
        return dicts_list

    def string_formatter(self, string):
        result = re.compile(r'<[^>]+>').sub('', string).replace(" ", " ").replace(" ", " ").replace("  ", " "). \
            replace("  ", " ").strip()
        if result in self.translate_dict:
            result = self.translate_dict[result]
        return result


class Vacancy:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.description = dictionary["description"]
        self.key_skills = dictionary["key_skills"]
        self.experience_id = dictionary["experience_id"]
        self.premium = dictionary["premium"]
        self.employer_name = dictionary["employer_name"]
        self.salary = Salary(dictionary["salary_from"], dictionary["salary_to"], dictionary["salary_gross"],
                             dictionary["salary_currency"])
        self.area_name = dictionary["area_name"]
        self.published_at = dictionary["published_at"]

    def get_fields(self):
        return {"Название": self.name, "Описание": self.description, "Навыки": self.key_skills,
                "Опыт работы": self.experience_id, "Премиум-вакансия": self.premium, "Компания": self.employer_name,
                "Оклад": self.salary, "Название региона": self.area_name, "Дата публикации вакансии": self.published_at}

    def create_copy(self):
        return Vacancy({"name": self.name, "description": self.description, "key_skills": self.key_skills,
                        "experience_id": self.experience_id, "premium": self.premium,
                        "employer_name": self.employer_name, "salary_from": self.salary.salary_from,
                        "salary_to": self.salary.salary_to, "salary_gross": self.salary.salary_gross,
                        "salary_currency": self.salary.salary_currency, "area_name": self.area_name,
                        "published_at": self.published_at})


class Salary:
    def __init__(self, salary_from, salary_to, salary_gross, salary_currency):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_gross = salary_gross
        self.salary_currency = salary_currency

    def rounder(self, number):
        return int(float(number))

    def get_salary_rub(self):
        return (self.rounder(self.salary_from) + self.rounder(self.salary_to)) / 2 * currency[self.salary_currency]


class InputCorrect:
    def __init__(self, columns_list):
        self.filter = filter.split(": ")
        self.sort_params = sort_param
        self.isReverse = isReverse
        self.diapason = diapason
        self.columns_list = columns_list

    def rounder(self, number):
        return int(float(number))

    def check_parameters(self):
        if self.filter[0] != "" and len(self.filter) == 1:
            print("Формат ввода некорректен")
            exit()
        elif self.filter[0] not in false_attribute:
            print("Параметр поиска некорректен")
            exit()
        elif self.sort_params not in false_attribute:
            print("Параметр сортировки некорректен")
            exit()
        elif self.isReverse != "Да" and self.isReverse != "Нет" and self.isReverse != "":
            print("Порядок сортировки задан некорректно")
            exit()

    def sort_vacancies(self, data_vacancies):
        self.isReverse = self.isReverse == "Да"
        if self.sort_params == "":
            return data_vacancies
        elif self.sort_params == "Оклад":
            return sorted(data_vacancies,
                          key=lambda vacancy: vacancy.salary.get_salary_rub(),
                          reverse=self.isReverse)

        elif self.sort_params == "Навыки":
            return sorted(data_vacancies, key=lambda vacancy: len(vacancy.key_skills.split("\n")),
                          reverse=self.isReverse)
        elif self.sort_params == "Опыт работы":
            experience_dictionary = {"Нет опыта": 0, "От 1 года до 3 лет": 1, "От 3 до 6 лет": 2, "Более 6 лет": 3}
            return sorted(data_vacancies, key=lambda vacancy: experience_dictionary[vacancy.experience_id],
                          reverse=self.isReverse)
        else:
            return sorted(data_vacancies, key=lambda vacancy: vacancy.get_fields()[self.sort_params],
                          reverse=self.isReverse)

    def row_pass_filter(self, vacancy):
        if self.filter[0] == "Оклад":
            if self.rounder(self.filter[1]) < self.rounder(vacancy.salary.salary_from) \
                    or self.rounder(self.filter[1]) > self.rounder(vacancy.salary.salary_to):
                return False
        elif self.filter[0] == "Навыки":
            for element in self.filter[1].split(", "):
                if element not in vacancy.key_skills.split("\n"):
                    return False
        elif self.filter[0] == "Идентификатор валюты оклада":
            if self.filter[1] != vacancy.salary.salary_currency:
                return False
        elif self.filter[0] == "Дата публикации вакансии":
            if self.filter[1] != self.date_formatter(vacancy.published_at):
                return False
        elif self.filter[0] in vacancy.get_fields() \
                and self.filter[1] != vacancy.get_fields()[self.filter[0]]:
            return False
        return True

    def create_table(self, table, count):
        s = 0
        e = count
        self.diapason = self.diapason.split(" ")
        if self.diapason[0] == "":
            pass
        elif len(self.diapason) == 1:
            s = int(self.diapason[0]) - 1
        elif len(self.diapason) == 2:
            s = int(self.diapason[0]) - 1
            e = int(self.diapason[1]) - 1
        self.columns_list = self.columns_list.split(", ")
        if self.columns_list[0] == "":
            return table.get_string(start=s, end=e)
        else:
            self.columns_list.insert(0, "№")
            return table.get_string(start=s, end=e, ﬁelds=self.columns_list)

    def print_vacancies(self, vacancies):
        number = 1
        table = PrettyTable(hrules=prettytable.ALL, align='l')
        new_data_vacancies = self.sort_vacancies(vacancies)
        table.field_names = ["№", "Название", "Описание", "Навыки", "Опыт работы", "Премиум-вакансия", "Компания",
                             "Оклад", "Название региона", "Дата публикации вакансии"]
        for new_vacancy in new_data_vacancies:
            formatted_new_vacancy = self.row_formatter(new_vacancy)
            if not self.row_pass_filter(new_vacancy):
                continue
            row = [value if len(value) <= 100 else value[:100] + "..." for value in
                   formatted_new_vacancy.get_fields().values()]
            row.insert(0, number)
            table.add_row(row)
            number += 1
        if number == 1:
            print("Ничего не найдено")
            exit()
        else:
            table.max_width = 20
            table = self.create_table(table, number - 1)
            print(table)

    def row_formatter(self, vacancy):
        min_salary = self.int_formatter(vacancy.salary.salary_from)
        max_salary = self.int_formatter(vacancy.salary.salary_to)
        before_tax = "Без вычета налогов" if vacancy.salary.salary_gross == "Да" else "С вычетом налогов"
        new_vacancy = vacancy.create_copy()
        new_vacancy.salary = f"{min_salary} - {max_salary} ({vacancy.salary.salary_currency}) ({before_tax})"
        new_vacancy.published_at = self.date_formatter(vacancy.published_at)
        return new_vacancy

    def int_formatter(self, number):
        number = str(self.rounder(number))
        number_len = len(number)
        number_len_mod = number_len % 3
        number_len_div = number_len // 3
        result_str = number[:number_len_mod]
        for i in range(number_len_div):
            if result_str != "":
                result_str += " "
            result_str += number[number_len_mod + i * 3: number_len_mod + (i + 1) * 3]
        return result_str

    def date_formatter(self, date):
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


currency = {"Белорусские рубли": 23.91, "Гривны": 1.64, "Грузинский лари": 21.74, "Доллары": 60.66, "Евро": 59.90,
            "Киргизский сом": 0.76, "Манаты": 35.68, "Рубли": 1, "Тенге": 0.13, "Узбекский сум": 0.0055}
false_attribute = ["Навыки", "Оклад", "Дата публикации вакансии", "Опыт работы", "Премиум-вакансия",
                   "Идентификатор валюты оклада", "Название", "Название региона", "Компания", ""]
file_name = input("Введите название файла: ")
filter = input("Введите параметр фильтрации: ")
sort_param = input("Введите параметр сортировки: ")
isReverse = input("Обратный порядок сортировки (Да / Нет): ")
diapason = input("Введите диапазон вывода: ")
columns = input("Введите требуемые столбцы: ")
input_correct = InputCorrect(columns)
input_correct.check_parameters()
dataset = DataSet()
input_correct.print_vacancies(dataset.vacancies_fields)

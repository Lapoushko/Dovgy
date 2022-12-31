from openpyxl.styles import Side, Border, Font
from openpyxl import Workbook


class ExcelCreator:
    def __init__(self, stats):
        self.workbook = self.initialize_workbook(stats)

    def initialize_workbook(self, statistics):
        workbook, years_sheet, cities_sheet = self.create_workbook(statistics)
        self.add_stats_to_excel(statistics, years_sheet, cities_sheet)
        self.set_sheets_settings(statistics, years_sheet, cities_sheet)
        workbook.save('report.xlsx')
        return workbook

    def create_workbook(self, statistics):
        workbook = Workbook()
        years_sheet = workbook.active
        years_sheet.title = 'Статистика по годам'
        cities_sheet = workbook.create_sheet('Статистика по городам')
        years_sheet.append(['Год', 'Средняя зарплата',
                            f'Средняя зарплата - {statistics.vacancy_name} по региону {statistics.area_name}',
                            'Количество вакансий', f'Количество вакансий - {statistics.vacancy_name} по региону {statistics.area_name}'])
        cities_sheet.append(['Город', 'Уровень зарплат', '', 'Город', 'Доля Вакансий'])
        return workbook, years_sheet, cities_sheet

    def add_stats_to_excel(self, statistics, years_sheet, cities_sheet):
        for year in statistics.years_df.index:
            years_sheet.append([year, statistics.years_df.loc[year]['salary'], statistics.years_df.loc[year]['prof_salary'],
                                statistics.years_df.loc[year]['count'], statistics.years_df.loc[year]['prof_count']])
        for city in statistics.cities_salary_df.index:
            cities_sheet.append([city, statistics.cities_salary_df.loc[city]['salary']])
        for i, city in enumerate(statistics.cities_percent_df.index, 2):
            cities_sheet[f'D{i}'].value = city
            cities_sheet[f'E{i}'].value = f'{round(statistics.cities_percent_df.loc[city]["percent"], 2)}%'

    def set_sheets_settings(self, stats, years_sheet, cities_sheet):
        used_columns = ['A', 'B', 'C', 'D', 'E']
        for i in used_columns:
            years_sheet[f'{i}1'].font = Font(bold=True)
            cities_sheet[f'{i}1'].font = Font(bold=True)
            years_sheet.column_dimensions[i].width = max(map(lambda x: len(str(x.value)), years_sheet[i])) + 1
            cities_sheet.column_dimensions[i].width = max(
                map(lambda x: len(str(x.value)), cities_sheet[i])) + 1
        thins = Side(border_style="thin")
        for column in used_columns:
            for row in range(1, 12):
                years_sheet[f'{column}{row}'].border = Border(top=thins, bottom=thins, left=thins, right=thins)
        for column in used_columns:
            for row in range(1, len(stats.years_df.index) + 2):
                if column == 'C':
                    break
                cities_sheet[f'{column}{row}'].border = Border(top=thins, bottom=thins, left=thins, right=thins)

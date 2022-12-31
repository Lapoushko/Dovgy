import numpy as np
import sqlite3
import pandas as pd


class Statistics:
    def __init__(self, vacancy_name, area_name):
        self.vacancy_name = vacancy_name
        self.area_name = area_name
        self.vacancies_count = 0
        self.years_df = pd.DataFrame()
        self.cities_salary_df = pd.DataFrame()
        self.cities_percent_df = pd.DataFrame()

    def sort_dataframe(self, by):
        return self.cities_salary_df.sort_values(by=by, ascending=False).head(10)

    def get_percent_of_other_cities(self):
        return 100 - self.cities_percent_df['percent'].sum()

    def get_statistics(self):
        connect = sqlite3.connect('vacancies_database.db')
        cursor = connect.cursor()
        self.vacancies_count = cursor.execute(self.get_sql_requests['count']).fetchone()[0]
        years_df = pd.read_sql(self.get_sql_requests['years'], connect, index_col='year')
        prof_years_df = pd.read_sql(self.get_sql_requests['prof_years'], connect, index_col='year')
        self.cities_salary_df = pd.read_sql(self.get_sql_requests['cities_salary'], connect,
                                            index_col='area_name').fillna(0).astype({'salary': np.int})
        self.years_df = years_df.join(prof_years_df).fillna(0).astype({'salary': np.int, 'count': np.int, 'prof_salary': np.int, 'prof_count': np.int})
        self.cities_percent_df = pd.read_sql(self.get_sql_requests['cities_percent'], connect, index_col='area_name').fillna(0)

    def get_sql_requests(self):
        return {
            'years': 'SELECT CAST(SUBSTRING(published_at, 0, 5) as INTEGER) as year, '
                     'CAST(AVG(Salary) as INTEGER) as salary, '
                     'CAST(COUNT("index") as INTEGER) as count '
                     'FROM vacancies GROUP BY year',
            'prof_years': 'SELECT CAST(SUBSTRING(published_at, 0, 5) as INTEGER) as year, '
                          'CAST(AVG(Salary) as INTEGER) as prof_salary, '
                          'CAST(COUNT("index") as INTEGER) as prof_count '
                          'FROM vacancies '
                          f'WHERE name LIKE ("%{self.vacancy_name}%") '
                          f'AND area_name LIKE ("%{self.area_name}%") '
                          'GROUP BY year',
            'count': 'SELECT COUNT(*) FROM vacancies',
            'cities_salary': 'SELECT area_name, '
                             'CAST(AVG(Salary) as INTEGER) as salary '
                             'FROM vacancies '
                             'GROUP BY area_name '
                             'ORDER BY salary DESC '
                             'LIMIT 10',
            'cities_percent': 'SELECT area_name, '
                              f'(COUNT("index") * 100.0 / {self.vacancies_count}) as percent '
                              'FROM vacancies '
                              'GROUP BY area_name '
                              'HAVING percent > 1 '
                              'ORDER BY percent DESC '
                              'LIMIT 10'
        }

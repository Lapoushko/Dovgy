import pandas as pd
import sqlite3


class formatterToSQL:
    def __init__(self, nameFile):
        self.__con = sqlite3.connect("currencies_db.sqlite")
        self.nameFile = nameFile
        self.__available_currencies = list(
            pd.read_sql("SELECT * from currencies WHERE date='2003-01'", self.__con).keys()[1:])

    def getSalary(self, row: pd.DataFrame) -> float or str:
        fromSalary, toSalary, curSalary, published = str(row[0]), str(row[1]), str(row[2]), str(row[3])
        if curSalary == 'nan': return 'nan'
        if fromSalary != 'nan' and toSalary != 'nan': s = float(fromSalary) + float(toSalary)

        elif fromSalary == 'nan' and toSalary != 'nan':  s = float(toSalary)

        elif fromSalary != 'nan' and toSalary == 'nan':  s = float(fromSalary)
        else:  return 'nan'

        if curSalary != 'RUR' and curSalary in self.__available_currencies:
            date = published[:7]
            multiplicate = pd.read_sql(f"SELECT {curSalary} from currencies WHERE date='{date}'", self.__con)[
                f'{curSalary}'][0]
            if multiplicate is not None:
                s *= multiplicate
            else:
                return 'nan'
        return round(s)

    def salariesProc(self):
        dataframe = pd.read_csv(self.nameFile)
        dataframe['salary'] = dataframe[['salary_from', 'salary_to', 'salary_currency', 'published_at']].apply(self.getSalary,
                                                                                                 axis=1)
        dataframe['published_at'] = dataframe['published_at'].apply(lambda x: x[:7])
        dataframe.drop(labels=['salary_to', 'salary_from', 'salary_currency'], axis=1, inplace=True)
        dataframe = dataframe.loc[dataframe['salary'] != 'nan']
        dataframe.to_csv('all.csv', index=False)

    def csvSqliteVacs(self, nameFile):
        dataframe = pd.read_csv(nameFile)
        connect = sqlite3.connect('all_vacancies')
        c = connect.cursor()
        c.execute(
            'CREATE TABLE IF NOT EXISTS all_vacancies (name text, area_name text, published_at text, salary number)')
        connect.commit()
        dataframe.to_sql('all_vacancies', connect, if_exists='replace', index=False)


formatterSQL = formatterToSQL('vacancies_dif_currencies.csv')
formatterSQL.salariesProc()
formatterSQL.csvSqliteVacs('all.csv')

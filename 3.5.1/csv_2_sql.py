import pandas as pd
import sqlite3


def createSqlFromCSV(file_name):
    # Создаёт SQL-таблицу из CSV-файла
    dataFrame = pd.read_csv(file_name)
    connect = sqlite3.connect('currencies_db')
    c = connect.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS currencies (date text, RUR number, USD number, KZT number, BYR number,'
              'UAH number, EUR number)')
    connect.commit()
    dataFrame.to_sql('currencies', connect, if_exists='replace', index=False)

createSqlFromCSV('dataframe.csv')

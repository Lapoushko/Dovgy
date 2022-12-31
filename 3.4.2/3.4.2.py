import pathlib
import time
import concurrent.futures
from Input import Input
from ParseCsvFileByYear import ParseCsvFileByYear
from Stat import Stat
from CreateStatFiles import CreateStatFiles

directory = 'vacancies_by_year'
if __name__ == "__main__":
    year_salary = {}
    professions_year_salary = {}
    year_vacancy = {}
    professions_year_vacancies = {}
    inputUser = Input()
    spl = ParseCsvFileByYear(inputUser.fileCsv, directory)
    start = time.time()
    files = [str(file) for file in pathlib.Path(f"./{directory}").iterdir()]
    stats = Stat(inputUser.profession)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        raw = list(executor.map(stats.process_data, files))
        for e in raw:
            for i, value in zip(range(4), [year_salary, year_vacancy, professions_year_salary, professions_year_vacancies]):
                value.update(e[i])
    CreateStatFiles(year_salary, year_vacancy, professions_year_salary, professions_year_vacancies, inputUser.profession).create_files()

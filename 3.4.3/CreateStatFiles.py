from Report import Report
from PdfCreater import PdfCreater


class CreateStatFiles:
    """
    Класс для создания итоговых файлов
    """

    def __init__(self, year_salary, year_vacancy, professions_year_salary, professions_year_vacancies, profession):
        self.year_salary = year_salary
        self.year_vacancy = year_vacancy
        self.professions_year_salary = professions_year_salary
        self.professions_year_vacancies = professions_year_vacancies
        self.profession = profession

    def create_files(self):
        output_data = {"Динамика уровня зарплат по годам:": self.year_salary,
                       "Динамика количества вакансий по годам:": self.year_vacancy,
                       "Динамика уровня зарплат по годам для выбранной профессии:": self.professions_year_salary,
                       "Динамика количества вакансий по годам для выбранной профессии:": self.professions_year_vacancies}
        [print(i, output_data[i]) for i in output_data]
        excel_file = "report.xlsx"
        report = Report(profes=self.profession,
                        years=[i for i in self.year_salary],
                        avgSalary=[self.year_salary[i] for i in self.year_salary],
                        avgSalaryProf=[self.professions_year_salary[i] for i in
                                       self.professions_year_salary],
                        countVacsYear=[self.year_vacancy[i] for i in self.year_vacancy],
                        countVacsYearProf=[self.professions_year_vacancies[i] for i in
                                           self.professions_year_vacancies],
                        nameFile=excel_file)
        report.generateExcel()
        graph_name = "graph.png"
        pdf = PdfCreater(graph_name=graph_name, excel_file_name=excel_file, profession=self.profession)
        pdf.generatePdf()

from Report import Report
from PdfCreater import PdfCreater

class CreateStatFiles:
    # Класс для создания итоговых файлов
    def create_files(self):
        outputDataInfo = {"Динамика уровня зарплат по годам:": self.salaryYear,
                       "Динамика количества вакансий по годам:": self.vacancyYear,
                       "Динамика уровня зарплат по годам для выбранной профессии:": self.profSalaryYear,
                       "Динамика количества вакансий по годам для выбранной профессии:": self.profVacanciesYear}
        [print(i, outputDataInfo[i]) for i in outputDataInfo]
        excel = "report.xlsx"
        report = Report(profes=self.profession,
                        countYear=[i for i in self.salaryYear],
                        salaryAvg=[self.salaryYear[i] for i in self.salaryYear],
                        avgSalaryProf=[self.profSalaryYear[i] for i in self.profSalaryYear],
                        countVacsYear=[self.vacancyYear[i] for i in self.vacancyYear],
                        countVacsYearProf=[self.profVacanciesYear[i] for i in self.profVacanciesYear],
                        nameFile=excel)
        report.generateExcel()
        nameGraph = "graph.png"
        pdfFile = PdfCreater(nameGraph=nameGraph, excelNameFile=excel, profes=self.profession)
        pdfFile.generatePdf()
    def __init__(self, salaryYear, vacancyYear, profSalaryYear, profVacanciesYear, profes):
        self.salaryYear = salaryYear
        self.vacancyYear = vacancyYear
        self.profSalaryYear = profSalaryYear
        self.profVacanciesYear = profVacanciesYear
        self.profession = profes
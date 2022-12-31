from Report import Report
from PdfCreater import PdfCreater


class CreateStatFiles:
    # Класс для создания итоговых файлов

    def __init__(self, salaryYear, vacYear, salaryYearProfes, vacsYearProf, profes):
        self.salaryYear = salaryYear
        self.vacYear = vacYear
        self.salaryYearProfes = salaryYearProfes
        self.vacsYearProf = vacsYearProf
        self.profession = profes

    def create_files(self):
        outputArray = {"Динамика уровня зарплат по годам:": self.salaryYear,
                       "Динамика количества вакансий по годам:": self.vacYear,
                       "Динамика уровня зарплат по годам для выбранной профессии:": self.salaryYearProfes,
                       "Динамика количества вакансий по годам для выбранной профессии:": self.vacsYearProf}
        [print(i, outputArray[i]) for i in outputArray]
        excel = "rep.xlsx"
        rep = Report(profession=self.profession,
                     years=[i for i in self.salaryYear],
                     salaryAvg=[self.salaryYear[i] for i in self.salaryYear],
                     salaryProfAvg=[self.salaryYearProfes[i] for i in
                                    self.salaryYearProfes],
                     countVacsYear=[self.vacYear[i] for i in self.vacYear],
                     countVacsYearProf=[self.vacsYearProf[i] for i in
                                        self.vacsYearProf],
                     nameFile=excel)
        rep.generateNewExcel()
        graphName = "graph.png"
        pdfFile = PdfCreater(nameGraph=graphName, excel=excel, prof=self.profession)
        pdfFile.generateNewPdf()

from Report import Report
from PdfCreater import PdfCreater


class CreateStatFiles:

    # Класс для создания итоговых файлов


    def __init__(self, salaryYear, vacYear, salaryYearProf, yearVacsProf, prof):
        self.salaryYear = salaryYear
        self.vacYear = vacYear
        self.salaryYearProf = salaryYearProf
        self.yearVacsProf = yearVacsProf
        self.profession = prof

    def createNewFiles(self):
        putputArray = {"Динамика уровня зарплат по годам:": self.salaryYear,
                       "Динамика количества вакансий по годам:": self.vacYear,
                       "Динамика уровня зарплат по годам для выбранной профессии:": self.salaryYearProf,
                       "Динамика количества вакансий по годам для выбранной профессии:": self.yearVacsProf}
        [print(i, putputArray[i]) for i in putputArray]
        excelFile = "rep.xlsx"
        rep = Report(profes=self.profession,
                     years=[i for i in self.salaryYear],
                     avgSalary=[self.salaryYear[i] for i in self.salaryYear],
                     avgSalaryProf=[self.salaryYearProf[i] for i in
                                    self.salaryYearProf],
                     countVacsYear=[self.vacYear[i] for i in self.vacYear],
                     countVacsYearProf=[self.yearVacsProf[i] for i in
                                        self.yearVacsProf],
                     nameFile=excelFile)
        rep.generateExcel()
        nameGraph = "graph.png"
        pdFile = PdfCreater(nameGraph=nameGraph, excel=excelFile, profes=self.profession)
        pdFile.generate_pdf()

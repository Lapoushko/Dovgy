import os
from jinja2 import Environment, FileSystemLoader
import pdfkit
from xlsx2html import xlsx2html


class PdfCreater:
    # Класс для конвертирования данных статистики в pdf-файл

    def generateNewPdf(self):
        environment = Environment(loader=FileSystemLoader('.'))
        temp = environment.get_template("pdf_template.html")
        graphPath = os.path.abspath(self.graph)
        outputStream = xlsx2html(self.excel, sheet="Статистика по годам")
        outputStream.seek(0)
        tempPdf = temp.render({"prof": self.prof, "graph": graphPath, "first_table": outputStream.read()})
        config = pdfkit.configuration(wkhtmltopdf=r"D:\For PDF python\wkhtmltopdf\bin\wkhtmltopdf.exe")
        pdfkit.from_string(tempPdf, 'report.pdf', configuration=config, options={"enable-local-file-access": ""})
    def __init__(self, nameGraph, excel, prof):
        self.graph = nameGraph
        self.excel = excel
        self.prof = prof



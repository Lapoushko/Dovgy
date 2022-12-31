import os
from jinja2 import Environment, FileSystemLoader
import pdfkit
from xlsx2html import xlsx2html


class PdfCreater:
    # Класс для конвертирования данных статистики в pdf-файл

    def generate_pdf(self):
        environment = Environment(loader=FileSystemLoader('.'))
        temp = environment.get_template("pdf_template.html")
        pathGraph = os.path.abspath(self.graph)
        streamOut = xlsx2html(self.excel, sheet="Статистика по годам")
        streamOut.seek(0)
        pdfTemp = temp.render({"prof": self.prof, "graph": pathGraph, "first_table": streamOut.read()})
        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        pdfkit.from_string(pdfTemp, 'report.pdf', configuration=config, options={"enable-local-file-access": ""})

    def __init__(self, nameGraph, excelNameFile, profes):
        self.graph = nameGraph
        self.excel = excelNameFile
        self.prof = profes

import os
from jinja2 import Environment, FileSystemLoader
import pdfkit
from xlsx2html import xlsx2html


class PdfCreater:

    # Класс для конвертирования данных статистики в pdf-файл


    def __init__(self, graph_name, excel_file_name, profession):
        self.graph = graph_name
        self.excel_file = excel_file_name
        self.prof = profession

    def generatePdf(self):
        environment = Environment(loader=FileSystemLoader('.'))
        temp = environment.get_template("pdf_template.html")
        graphPath = os.path.abspath(self.graph)
        outputStream = xlsx2html(self.excel_file, sheet="Статистика по годам")
        outputStream.seek(0)
        tempPdf = temp.render({"prof": self.prof, "graph": graphPath, "first_table": outputStream.read()})
        config = pdfkit.configuration(wkhtmltopdf=r"D:\For PDF python\wkhtmltopdf\bin\wkhtmltopdf.exe")
        pdfkit.from_string(tempPdf, 'report.pdf', configuration=config, options={"enable-local-file-access": ""})

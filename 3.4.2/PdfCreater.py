import os
from jinja2 import Environment, FileSystemLoader
import pdfkit
from xlsx2html import xlsx2html


class PdfCreater:
    """Класс для конвертирования данных статистики в pdf-файл"""

    def __init__(self, graph_name, excel_file_name, profession):
        self.graph = graph_name
        self.excel_file = excel_file_name
        self.prof = profession

    def generate_pdf(self):
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("pdf_template.html")
        graph_path = os.path.abspath(self.graph)
        out_stream = xlsx2html(self.excel_file, sheet="Статистика по годам")
        out_stream.seek(0)
        pdf_template = template.render({"prof": self.prof, "graph": graph_path, "first_table": out_stream.read()})
        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        pdfkit.from_string(pdf_template, 'report.pdf', configuration=config, options={"enable-local-file-access": ""})

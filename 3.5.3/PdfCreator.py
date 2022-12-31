import pdfkit
from jinja2 import Environment, FileSystemLoader


class PdfCreator:
    def __init__(self, vacancy_name, area_name, workbook, years_sheet_rows):
        config = pdfkit.configuration(wkhtmltopdf=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        options = {'enable-local-file-access': None}
        pdfkit.from_string(self.fill_pdf_template(vacancy_name, area_name, workbook["Статистика по годам"],
                                                  workbook["Статистика по городам"], years_sheet_rows),
                           'report.pdf', configuration=config, options=options)

    def fill_pdf_template(self, vacancy_name, area_name, years_sheet, cities_sheet, years_sheet_rows):
        env = Environment(loader=FileSystemLoader('./ReportModule'))
        template = env.get_template('pdf_template.html')
        pdf_template = template.render({'vacancie_name': vacancy_name, 'area_name': area_name,
                                        'years_table': self.create_html_table(years_sheet, years_sheet_rows),
                                        'cities_table_first': self.create_html_table(cities_sheet, 10, last_column=2),
                                        'cities_table_second': self.create_html_table(cities_sheet, 10, 4)})
        return pdf_template

    def create_html_table(self, ws, rows_count, first_column=1, last_column=5):
        html = ''
        is_first = True
        for row in ws.iter_rows(min_row=1, min_col=first_column, max_col=last_column, max_row=rows_count + 1):
            html += '<tr>'
            for cell in row:
                html += '<td><b>' + str(cell.value) + '</b></td>' if is_first else '<td>' + str(cell.value) + '</td>'
            html += '</tr>'
            is_first = False
        return html

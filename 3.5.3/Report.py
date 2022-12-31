from Statistics import Statistics
from GraphsCreator import GraphsCreator
from PdfCreator import PdfCreator
from ExcelCreator import ExcelCreator


class Report:
    def __init__(self, vacancy_name, area_name):
        self.statistics = Statistics(vacancy_name, area_name)
        self.statistics.get_statistics()
        GraphsCreator(self.statistics)
        PdfCreator(vacancy_name, area_name, ExcelCreator(self.statistics).workbook, len(self.statistics.years_df.index))

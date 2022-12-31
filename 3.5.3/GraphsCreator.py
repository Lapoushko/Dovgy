from matplotlib import pyplot as plt
from Statistics import Statistics


class GraphsCreator:
    def __init__(self, statistics):
        self.generate_image(statistics)

    def generate_image(self, statistics: Statistics) -> None:
        plt.subplots(figsize=(10, 7))
        plt.grid(True)

        self.create_salary_by_year_plot(statistics)
        self.create_count_by_year_plot(statistics)
        self.create_salary_by_city_plot(statistics)
        self.create_count_by_city_plot(statistics)

        plt.subplots_adjust(wspace=0.5, hspace=0.5)
        plt.savefig('graph.png')

    def create_salary_by_year_plot(self, statistics: Statistics) -> None:
        first = plt.subplot(221)
        plt.tick_params(axis='x', which='major', labelsize=8, rotation=90)
        plt.tick_params(axis='y', which='major', labelsize=8)
        first.bar(list(map(lambda y: y - 0.2, statistics.years_df.index)),
                  statistics.years_df['salary'], width=0.4,
                  label='Средняя з/п')
        first.bar(list(map(lambda y: y + 0.2, statistics.years_df.index)),
                  statistics.years_df['prof_salary'], width=0.4,
                  label=f'З/п {statistics.vacancy_name} по региону {statistics.area_name}')
        plt.legend(fontsize=8)
        plt.title('Уровень зарплат по годам', fontsize=12)

    def create_count_by_year_plot(self, statistics: Statistics) -> None:
        second = plt.subplot(222)
        plt.tick_params(axis='x', which='major', labelsize=8, rotation=90)
        plt.tick_params(axis='y', which='major', labelsize=8)
        second.bar(list(map(lambda y: y - 0.2, statistics.years_df.index)),
                   statistics.years_df['count'], width=0.4,
                   label='Количество вакансий')
        second.bar(list(map(lambda y: y + 0.2, statistics.years_df.index)),
                   statistics.years_df['prof_count'].to_list(), width=0.4,
                   label=f'Количество вакансий {statistics.vacancy_name} по региону {statistics.area_name}')
        plt.legend(fontsize=8)
        plt.title('Количество вакансий по годам', fontsize=12)

    def create_salary_by_city_plot(self, statistics: Statistics) -> None:
        third = plt.subplot(223)
        plt.tick_params(axis='x', which='major', labelsize=8)
        plt.tick_params(axis='y', which='major', labelsize=6)
        third.barh(statistics.cities_salary_df.index, statistics.cities_salary_df['salary'])
        plt.title('Уровень зарплат по городам', fontsize=12)

    def create_count_by_city_plot(self, statistics: Statistics) -> None:
        statistics.get_percent_of_other_cities()
        fourth = plt.subplot(224)
        plt.rc('xtick', labelsize=6)
        cities_df = statistics.cities_percent_df
        cities_df.loc['Другие'] = statistics.get_percent_of_other_cities()
        fourth.pie(cities_df['percent'],
                   labels=cities_df.index,
                   colors=['r', 'g', 'b', 'm', 'y', 'c', 'orange', 'darkblue', 'pink', 'sienna', 'grey'])
        plt.title('Доля вакансий по городам', fontsize=12)

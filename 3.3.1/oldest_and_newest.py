from stats import *

data: List[Vacancy] = csv_filer(*csv_reader('vacancies_dif_currencies.csv'))

oldest_vacancy = None
newest_vacancy = None

for vacancy in data:
	if not oldest_vacancy:
		oldest_vacancy = vacancy
	if not newest_vacancy:
		newest_vacancy = vacancy

	if vacancy.published_at < oldest_vacancy.published_at:
		oldest_vacancy = vacancy

	if vacancy.published_at > newest_vacancy.published_at:
		newest_vacancy = vacancy

print(f'Дата публикации самой старой вакансии: {oldest_vacancy.published_at}\nДата публикации самой новой вакансии: {newest_vacancy.published_at}')

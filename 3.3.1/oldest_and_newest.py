from stats import *

oldVac = None
newVac = None

data: List[Vacancy] = csv_filer(*csv_reader('vacancies_dif_currencies.csv'))

for vac in data:
	if not oldVac: oldVac = vac
	if not newVac: newVac = vac
	if vac.published_at < oldVac.published_at: oldVac = vac
	if vac.published_at > newVac.published_at: newVac = vac


print(f'Дата публикации самой старой вакансии: {oldVac.published_at}\nДата публикации самой новой вакансии: {newVac.published_at}')

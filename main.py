from hh_parser import hh_get_pages, hh_get_vacancies
from sj_parser import sj_get_pages, sj_get_vacancies

hh_pages = hh_get_pages("https://hh.ru/search/vacancy?text=python&order_by=relevance&items_on_page=20")
hh_vacancies = []
for page in hh_pages:
    hh_vacancies.extend(hh_get_vacancies(page))

print(*hh_vacancies, sep='\n')

sj_pages = sj_get_pages("https://russia.superjob.ru/vacancy/search/?keywords=python&click_from=facet")

sj_vacancies = []
for page in sj_pages:
    sj_vacancies.extend(sj_get_vacancies(page))

print(*sj_vacancies, sep='\n')

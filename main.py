from hh_parser import hh_get_pages, hh_get_vacancies

hh_pages = hh_get_pages("https://hh.ru/search/vacancy?text=python&order_by=relevance&items_on_page=20")

for page in hh_pages:
    a = hh_get_vacancies(page)
    print(a)




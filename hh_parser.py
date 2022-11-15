import requests
from bs4 import BeautifulSoup  # searching on the page

headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive'
}  # headers for requests


def hh_get_pages(key_word: str):
    first_url = f"https://hh.ru/search/vacancy?text={key_word}&order_by=relevance&items_on_page=20"
    hh_request = requests.get(first_url, headers=headers)  # get HTML of the first page
    hh_soup = BeautifulSoup(hh_request.text, features="html.parser")  # define of seeker
    paginator = hh_soup.find("div", {'class': "pager", 'data-qa': "pager-block"})  # get block with the page urls
    last_page = int(paginator.find_all('a')[-2].text)  # the last page
    list_pages = []
    for page in range(last_page//10) if range(last_page//10) != 0 else 1:  # take not all pages
        list_pages.append(requests.get(first_url+f"&page={page}", headers=headers, timeout=15))
    return list_pages  # return list of all pages


def hh_get_title(hh_item: BeautifulSoup):
    return hh_item.find("span", {'data-page-analytics-event': "vacancy_search_suitable_item"}).find("a").text


def hh_get_company(hh_item: BeautifulSoup):
    return hh_item.find("div", {'class': "vacancy-serp-item__meta-info-company"}).find("a").text


def hh_get_location(hh_item: BeautifulSoup):
    return hh_item.find("div", {'data-qa': "vacancy-serp__vacancy-address"}).text.partition(',')[0]


def hh_get_link(hh_item: BeautifulSoup):
    return hh_item.find("span", {'data-page-analytics-event': "vacancy_search_suitable_item"}).find('a')['href']


def hh_get_vacancies(key_word: str):
    hh_pages = hh_get_pages(key_word)
    vacancies = []
    for hh_page in hh_pages:
        hh_items = BeautifulSoup(hh_page.text, features='html.parser').find_all("div", {'class': "vacancy-serp-item__layout"})
        for vacancy in hh_items:
            vacancies.append({'title': hh_get_title(vacancy), 'company': hh_get_company(vacancy), 'location': hh_get_location(vacancy), 'link': hh_get_link(vacancy)})
    return vacancies

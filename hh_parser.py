import requests
from bs4 import BeautifulSoup  # searching on the page

headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive'
}  # headers for requests


def hh_get_pages(first_url: str):
    hh_request = requests.get(first_url, headers=headers)  # get HTML of the first page
    hh_soup = BeautifulSoup(hh_request.text, features="html.parser")  # define of seeker
    # print(hh_request.html.html)
    paginator = hh_soup.find("div", {'class': "pager", 'data-qa': "pager-block"})  # get block with the page urls
    last_page = int(paginator.find_all('a')[-2].text)  # the last page
    list_pages = []
    for page in range(last_page//10):
        list_pages.append(requests.get(first_url+f"&page={page}", headers=headers))
    return list_pages  # return list of all pages


def hh_get_vacancies(hh_response: requests.models.Response):
    list_vacancies = []
    page = BeautifulSoup(hh_response.text, 'html.parser').find_all("span", {'data-page-analytics-event': "vacancy_search_suitable_item"})
    for vacancy in page:
        list_vacancies.append(vacancy.text)
    return list_vacancies


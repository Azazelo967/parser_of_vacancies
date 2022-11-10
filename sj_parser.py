import requests
from bs4 import BeautifulSoup

headers = {
    'Host': 'hh.ru',
    'User-Agent': 'Safari',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}


def sj_get_pages(first_url: str):
    sj_request = requests.get(first_url, headers)
    sj_soup = BeautifulSoup(sj_request.text, features="html.parser")
    max_page = int(sj_soup.find("div", {'class': "_3cQ7I _9mI07 _3T5uq _2lLER _1oLBB _3Sc4g _1JpIP"}).find_all("a")[-2].text)
    list_pages = []
    for page in range(1, max_page+1):
        list_pages.append(requests.get(first_url+f"&page={page}", headers))
    return list_pages


def sj_get_title(vacancy: BeautifulSoup):
    return vacancy.find("span", {'class': "_3FqEL _2JQOY _1dTXK _3h_V4 _1hdbq"}).find("a").text


def sj_get_company(vacancy: BeautifulSoup):
    company_block = vacancy.find("div", {'class': "_3cQ7I _2EaO5 U10QV _21flV"})
    return "" if company_block is None else company_block.find("a").text


def sj_get_location(vacancy: BeautifulSoup):
    location = vacancy.find("div", {'class': "HA2Nf eOMxK _3JTbG"})
    return "" if location is None else location.text


def sj_get_link(vacancy: BeautifulSoup):
    return "https://russia.superjob.ru"+vacancy.find("span", {'class': "_3FqEL _2JQOY _1dTXK _3h_V4 _1hdbq"}).find("a")["href"]


def sj_get_vacancies(sj_response_page: requests.models.Response):
    items = BeautifulSoup(sj_response_page.text, "html.parser").find_all("div", {'class': "_2lp1U _3NBrD _1WtQU"})
    vacancies = []
    for vacancy in items[:25]:
        vacancies.append({'title': sj_get_title(vacancy), 'company': sj_get_company(vacancy), 'location': sj_get_location(vacancy), 'link': sj_get_link(vacancy)})
    return vacancies


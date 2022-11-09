import requests
from bs4 import BeautifulSoup  # searching on the page

headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive'
}  # headers for get requests

hh_request = requests.get('https://hh.ru/search/vacancy?text=python&order_by=relevance&items_on_page=100', headers=headers)  # get HTML of the first page

hh_soup = BeautifulSoup(hh_request.text, 'html.parser')  # define of seeker

paginator = hh_soup.find("div", {'class': "pager", 'data-qa': "pager-block"})  # get block with the page urls

last_page = int(paginator.find_all('a')[-2].text)  # the last page

arr_hh_requests = []
for i in range(last_page):
  pass

print(*paginator.find_all('a'), sep='\n')

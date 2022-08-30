import pandas as pd
from bs4 import BeautifulSoup
import requests


titles = []
links = []
publish_times = []
exp_url = "https://www.diariomunicipal.sc.gov.br/?r=site/index&q=abertura+categoria%3ALicita%C3%A7%C3%B5es&AtoASolrDocument_page=1"
page = requests.get(exp_url)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")
for row in soup.find_all("div", {"class": "row no-print resultado-pesquisa"}):
    for link in row.find_all('h4'):
        links.append(link.find('a')['href'])
    for title in row.find_all('h4'):
        titles.append(title.text)
    for time in row.find_all('span', {"class": "quiet"}):
        publish_times.append(time.text[:16])

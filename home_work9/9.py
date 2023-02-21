import requests

from bs4 import BeautifulSoup


source = requests.get("https://minfin.com.ua/currency/nbu/")
soup = BeautifulSoup(source.text, features="html.parser")
soup_text = soup.find_all("p", {"class": "sc-1x32wa2-9 glerpA"})
#res = soup_text[0].find("div")
print(soup.text)
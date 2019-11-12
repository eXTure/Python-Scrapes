import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
reg_url = "https://www.thefamouspeople.com/famous-people-died-today.php"
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()
soup = BeautifulSoup(html, "html.parser")
extraction = soup.find_all('h5')
print('Famous people who died on this day:')
for line in extraction:
    print(line.text)

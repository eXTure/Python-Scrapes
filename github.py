import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
reg_url = "https://github.com/eXTure"
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(html, "html.parser")

# Take out the <div> of name and get its value
name_box = soup.find("span", attrs={"class": "float-left ws-normal text-left"})

# strip() is used to remove starting and trailing
name = name_box.text.strip()

print(name)

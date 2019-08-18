import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
#http://www.bloomberg.com/quote/SPX:IND
#https://www.kilo.lt
reg_url = "https://www.bloomberg.com/quote/SPX:IND"
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(html, "html.parser")

# Take out the <div> of name and get its value
name_box = soup.find("span", attrs={"class": "priceText__1853e8a5"})

# strip() is used to remove starting and trailing
name = name_box.text.strip()

print(name)

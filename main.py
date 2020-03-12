# coding: utf-8

from bs4 import BeautifulSoup
import requests
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv(override=True)

url = "https://tv.yahoo.co.jp/search/?q="

words = os.getenv("WORDS").split(",")

for word in words:
    parameter = urllib.parse.quote(word)
    r = requests.get(url + word)
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find("ul", "programlist")
    print(data.find("li").text)



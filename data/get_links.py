import requests
from bs4 import BeautifulSoup

_api_link_ = "http://api.lib.sfu.ca/"

def parseLinks():
    html = requests.get(_api_link_).text
    soup = BeautifulSoup(html, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    print(links)
    
parseLinks()
import requests
import time
from bs4 import BeautifulSoup as bs

page = requests.get("http://www.nhm.ac.uk/discover/the-cannibals-of-goughs-cave.html")
print(page.status_code)

soup = bs(page.content, 'html.parser')


article = soup.find_all("div", class_="article--container")

for i in soup.find_all("div", class_="article--container"):
    i_descendants = i.descendants
    for d in i_descendants:
        if d.name in ['h1', 'h2', 'p']:
            print(d.text)

#corpus = article.find_all(["h1", "h2", "p"])
#   corpus = i_descendants.find_all(['h1', 'h2', 'p'])
#   print(corpus.text)

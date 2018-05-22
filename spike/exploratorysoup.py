import requests
import time
import requests

page = requests.get("http://www.nhm.ac.uk/discover/the-cannibals-of-goughs-cave.html")
print(page.status_code)

soup = bs(page.content, 'html.parser')

for i in soup.find_all("div", class_="article--container"):
    i_descendants = i.descendants
    for d in i_descendants:
        if d.name in ['h1', 'h2', 'p']:
            print(d.text)


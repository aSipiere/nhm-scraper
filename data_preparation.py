import requests
from bs4 import BeautifulSoup

def content_to_text(page):
    """Find all divs with class 'article--container' then loop through the descendants"""
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    text = ""

    for i in soup.find_all("div", class_="article--container"):
        i_descendants = i.descendants
        for d in i_descendants:
            if d.name in ['h1', 'h2', 'p']:
                text += "{}\n".format(d.text)
    return text

def aggregate_corpus(pages):
    """For each address we write the result of content_to_text to file"""
    corpus = []
    for i in pages:
        corpus.append(content_to_text(i))
    return corpus
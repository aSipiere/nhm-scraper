from data_preparation import *
from tokenization import *

pages = ["http://www.nhm.ac.uk/discover/the-cannibals-of-goughs-cave.html",
         "http://www.nhm.ac.uk/discover/how-we-became-human.html",
         "http://www.nhm.ac.uk/discover/the-origin-of-our-species.html"]

for i in pages:
    if requests.get(i).status_code != 200:
        raise requests.ConnectionError("Expected status code 200 at {}, but got {}".format(i, requests.get(i).status_code))
    else:
        print("Status 200-OK")

corpus = aggregate_corpus(pages)

print(get_tfidf(corpus))


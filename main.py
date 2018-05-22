from data_preparation import *
from tokenization import *

path = "data/corpora.txt"
pages = ["http://www.nhm.ac.uk/discover/the-cannibals-of-goughs-cave.html",
         "http://www.nhm.ac.uk/discover/how-we-became-human.html",
         "http://www.nhm.ac.uk/discover/the-origin-of-our-species.html"]

for i in pages:
    if requests.get(i).status_code != 200:
        raise requests.ConnectionError("Expected status code 200 at {}, but got {}".format(i, requests.get(i).status_code))
    else:
        print("Status 200-OK")

aggregate_corpora(pages, path)

vector = string_to_vect(path)



get_tfidf(vector)

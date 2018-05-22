import requests

pages = ["http://www.nhm.ac.uk/discover/the-cannibals-of-goughs-cave.html",
         "http://www.nhm.ac.uk/discover/how-we-became-human.html",
         "http://www.nhm.ac.uk/discover/the-origin-of-our-species.html"]
r = []

def test_connections_okay():
    """Generic assert 200 ok"""
    for i in pages:
        assert requests.get(i).status_code == 200, "Expected status code 200 at {}, but got {}".format(i, requests.get(i).status_code)


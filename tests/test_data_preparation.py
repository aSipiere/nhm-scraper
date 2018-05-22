import data_preparation

pages = ['http://www.nhm.ac.uk/discover/the-cannibals-of-goughs-cave.html',
         'http://www.nhm.ac.uk/discover/how-we-became-human.html',
         'http://www.nhm.ac.uk/discover/the-origin-of-our-species.html']

dummy_page = 'tests/fixtures/dummy_page.html'

dummy_pages = ['tests/fixtures/dummy_page.html',
               'tests/fixtures/dummy_page_2.html',
               'tests/fixtures/dummy_page_3.html'
]

def test_connections_okay(pages):
    """Generic assert 200 ok"""
    for i in pages:
        assert data_preparation.requests.get(i).status_code == 200, "Expected status code 200 at {}, but got {}".format(i, data_preparation.requests.get(i).status_code)

def test_content_to_text(dummy_page):
    """Assert that bad elements of dummy file not in corpus"""
    corpus = data_preparation.content_to_text(dummy_page)
    assert "bad" not in corpus

test_content_to_text(dummy_page)

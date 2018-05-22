from data_preparation import *
import unittest

"""
TODO: 
    * Better test for aggregate_corpus
"""

class TestDataPreparationMethods(unittest.TestCase):

    def test_content_to_text(self):
        """
        Assert that bad elements of dummy file not in corpus
        The following are the same:
        https://asipiere.github.io/nhm-scraper/
        index.html
        tests/fixtures/dummy_page.html
        """
        corpus = content_to_text('https://asipiere.github.io/nhm-scraper/')
        self.assertNotIn('bad', corpus)

    def test_aggregate_corpus(self):
        """Check that we've appended three items to the list"""
        dummy_pages = ['https://asipiere.github.io/nhm-scraper/',
                       'https://asipiere.github.io/nhm-scraper/',
                       'https://asipiere.github.io/nhm-scraper/']
        self.assertEqual(len(aggregate_corpus(dummy_pages)), 3)


if __name__ == '__main__':
    unittest.main()

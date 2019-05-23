import unittest as ut

from bs4 import BeautifulSoup
import os
from requests import get

import app.Scraper as scraper


class TestScraper(ut.TestCase):

    def test_getHTMLTextReturnsAValue(self):
        file_name = 'fake_placard.html'
        url = os.path.abspath('../tests/fake_placard.html')
        html_soup = scraper.get_html_text(url)
        self.assertIsNotNone(html_soup)

    def test_getHTMLTextReturnsABeatifulSoupObject(self):
        file_name = 'fake_placard.html'
        url = os.path.abspath('../tests/fake_placard.html')
        html_soup = scraper.get_html_text(url)
        self.assertIs(type(html_soup), BeautifulSoup)


if __name__ == '__main__':
    ut.main()

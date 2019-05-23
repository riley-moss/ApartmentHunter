from unittest import TestCase, main as unittest_main
from app.main import Scraper

from bs4 import BeautifulSoup
import os


class TestScraper(TestCase):

    def setUp(self):
        self.fake_url = os.path.abspath('../tests/fake_placard.html')

    def test_getHTMLTextReturnsAValue(self):
        html_soup = ""
        self.assertIsNotNone(html_soup)

    def test_givenHTMLFileReturnsABeautifulSoupObject(self):
        html_soup = Scraper.get_html_text(self.fake_url)
        self.assertIs(type(html_soup), BeautifulSoup)

    def test_givenBlankHTMLReturnEmptyList(self):
        self.assertEqual([], Scraper.parse_soup_for_placards(BeautifulSoup('', 'html.parser')))


if __name__ == '__main__':
    unittest_main()

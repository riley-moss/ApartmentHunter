from unittest import TestCase, main as unittest_main
from main import Scraper

from bs4 import BeautifulSoup
import os


class TestScraper(TestCase):

    def setUp(self):
        self.test_placard_file = os.path.abspath('../tests/test_placard.html')
        self.test_apartment_url = 'https://www.apartments.com/lakeview-3200-chicago-il/3qc6kde/'
        self.test_apartment_location = '3200 N Clark St, Chicago, IL 60657'
        self.test_apartment_rent = '$1,844 - 2,100'

    def test_givenBlankURLReturnBlankString(self):
        html_soup = ''
        self.assertEqual('', Scraper.get_html_text(html_soup))

    def test_givenHTMLFileReturnsABeautifulSoupObject(self):
        html_soup = Scraper.get_html_text(self.test_placard_file)
        self.assertIs(type(html_soup), BeautifulSoup)

    def test_givenBlankHTMLReturnEmptyList(self):
        self.assertEqual([], Scraper.parse_soup_for_placards(BeautifulSoup('', 'html.parser')))


if __name__ == '__main__':
    unittest_main()

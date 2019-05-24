import unittest as ut
from main import Scraper

from bs4 import BeautifulSoup
import os


class TestScraper(ut.TestCase):

    def setUp(self):
        self.test_placard_file = os.path.abspath('../tests/test_placard.html')
        self.test_apartment_url = 'https://www.apartments.com/lakeview-3200-chicago-il/3qc6kde/'
        self.test_apartment_location = '3200 N Clark St, Chicago, IL 60657'
        self.test_apartment_rent = '$1,844 - 2,100'

    def test_givenBlankResponseReturnBlankString(self):
        html_soup = ''
        self.assertEqual('', Scraper.get_html_text(html_soup))

    def test_givenHTMLResponseReturnsABeautifulSoupObject(self):
        response = open(self.test_placard_file)
        html_soup = Scraper.get_html_text(response)
        self.assertIs(type(html_soup), BeautifulSoup)
        response.close()

    def test_givenBlankHTMLReturnEmptyList(self):
        self.assertEqual([], Scraper.parse_soup_for_placards(''))

    @ut.skip
    def test_givenHTMLWithOnePlacardReturnListWithOneApartment(self):
        html_soup = Scraper.get_html_text(self.test_placard_file)
        apartment = Scraper.parse_soup_for_placards(html_soup)[0]
        self.assertEqual(self.test_apartment_url, apartment.url)
        self.assertEqual(self.test_apartment_location, apartment.location)
        self.assertEqual(self.test_apartment_rent, apartment.rent)


if __name__ == '__main__':
    ut.main()

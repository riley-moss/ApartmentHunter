import unittest as ut
from main import Scraper
from main.apartment import Apartment

from bs4 import BeautifulSoup
import os


class TestScraper(ut.TestCase):

    def setUp(self):
        self.test_placard_file = os.path.abspath('../tests/test_placard.html')
        self.test_apartment = Apartment('https://www.apartments.com/lakeview-3200-chicago-il/3qc6kde/',
                                        '3200 N Clark St, Chicago, IL 60657', '$1,844 - 2,100')
        self.test_response = open(self.test_placard_file)

    def test_givenBlankResponseReturnBlankString(self):
        html_soup = ''
        self.assertEqual('', Scraper.get_html_text(html_soup))

    def test_givenHTMLResponseReturnsABeautifulSoupObject(self):
        html_soup = Scraper.get_html_text(self.test_response)
        self.assertIs(type(html_soup), BeautifulSoup)

    def test_givenBlankHTMLResponseReturnEmptyList(self):
        self.assertEqual([], Scraper.parse_soup_for_placards(BeautifulSoup('', 'html.parser')))

    def test_givenHTMLWithApartmentPlacardReturnListWithOneApartment(self):
        html_soup = Scraper.get_html_text(self.test_response)
        apartment = Scraper.parse_soup_for_placards(html_soup)[0]
        self.assertEqual(self.test_apartment.url, apartment.url)
        self.assertEqual(self.test_apartment.location, apartment.location)
        self.assertEqual(self.test_apartment.rent, apartment.rent)

    def test_givenHTMLWithMultipleApartmentPlacardsReturnListWithMultipleApartments(self):
        html_soup = Scraper.get_html_text(self.test_response)
        apartments = Scraper.parse_soup_for_placards(html_soup)
        self.assertEqual(3, len(apartments))

    def tearDown(self):
        self.test_response.close()


if __name__ == '__main__':
    ut.main()

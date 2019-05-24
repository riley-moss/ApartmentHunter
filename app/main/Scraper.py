from bs4 import BeautifulSoup
from requests import get

from main.apartment import Apartment

headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})


def get_html_text(response):
    if response == '':
        return ''
    html_soup = BeautifulSoup(response, 'html.parser')
    return html_soup


def parse_soup_for_placards(html_soup):
    apartment_list = []
    placards = html_soup.find_all('article', class_="placard")
    for apartment in placards:
        url = apartment.get('data-url')
        location = apartment.find('div', class_="location").text
        rent = apartment.find('span', class_="altRentDisplay").text
        apartment_list.append(Apartment(url, location, rent))

    return apartment_list

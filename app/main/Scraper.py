from bs4 import BeautifulSoup

from app.main.Apartment import Apartment


def get_html_text(url):
    if url == '':
        return ''
    return BeautifulSoup(open(url), 'html.parser')


def parse_soup_for_placards(html_soup):
    return []

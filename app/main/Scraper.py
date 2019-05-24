from bs4 import BeautifulSoup

from main.Apartment import Apartment


def get_html_text(url):
    html_file = None
    try:
        html_file = open(url, 'r')
        html_soup = BeautifulSoup(html_file, 'html.parser')
    except FileNotFoundError:
        html_soup = ''
    finally:
        if html_file is not None:
            html_file.close()

    return html_soup


def parse_soup_for_placards(html_soup):
    return []

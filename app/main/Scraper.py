from bs4 import BeautifulSoup


def get_html_text(url):
    return BeautifulSoup(open(url), 'html.parser')

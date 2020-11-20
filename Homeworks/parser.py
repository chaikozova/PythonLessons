import requests
from bs4 import BeautifulSoup
import csv


HOST = 'https://kloop.kg/'
URL = 'https://kloop.kg/news/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'lmxl')
    items = soup.find_all('div', class_='elementor-posts-container elementor-posts elementor-posts--skin-classic elementor-grid elementor-has-item-ratio')
    news = []
    print(items)

    for item in items:
        news.append(
            {

            }
        )


html = get_html(URL)
get_content(html.text)
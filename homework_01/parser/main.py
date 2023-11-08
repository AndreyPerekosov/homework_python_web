import requests
from bs4 import BeautifulSoup as bs

# global var defines count of transitions to a link
DEPTH_LINKS = 1
# start discover for links from site defines in var below
INITIAL_SITE = 'https://habr.com/ru/articles/'


def get_links(link: str, urls: set, depth_links: int):
    if depth_links == 0:
        return
    try:
        response = requests.get(link)
    # in case if site is not available via need some type of vpn for example
    except Exception:
        print(f'site {link} is not available')
        return

    soup = bs(response.text, 'html.parser')
    for link in soup.find_all('a'):
        tmp_link = link.get('href')
        if tmp_link and tmp_link not in urls and tmp_link[0] == 'h':
            urls.add(link.get('href'))
            get_links(tmp_link, urls, depth_links - 1)


def print_links(links: set, writing_file: bool = False):
    if writing_file:
        with open('links.txt', 'w') as f:
            for link in links:
                f.write(link + '\n')
    else:
        print(links)


if __name__ == '__main__':
    result = set()
    get_links('https://habr.com/ru/articles/', result, DEPTH_LINKS)
    print_links(result, True)

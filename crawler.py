from requests import Session
from urllib.parse import unquote, urlparse, urljoin, urldefrag
from bs4 import BeautifulSoup, SoupStrainer

session = Session()
WEBSITE_URL = ''
CRAWL_TYPES = ['html', 'htm', '', 'phtml', 'php']

def get_file_extension(url: str) -> str:
    if '.' not in url:
        return ''
    else:
        return url.split('.')[-1]

def remove_url_params(url: str) -> str:
    return unquote(url).split('?')[0]

def make_absolute_link(href: str, current_page: str) -> str:
    return urljoin(current_page, href)

def find_links_on_page(url: str) -> list:
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('a'))
    links = [make_absolute_link(href['href'], url) for href in soup.find_all('a', href=True)]
    return [link for link in links if urlparse(link).netloc]

def crawl_website(start_url: str, max_depth: int = 2, ALLOW_SUBDOMAIN: bool = False) -> set:
    visited_urls = set()
    urls_to_visit = [(start_url, 1)]
    start_domain = urlparse(start_url).netloc
    if ALLOW_SUBDOMAIN:
        start_domain = start_domain.split('.', 1)[1]
    while urls_to_visit:
        current_url, current_depth = urls_to_visit.pop(0)
        current_url = urldefrag(current_url)[0]
        if current_url in visited_urls:
            continue
        visited_urls.add(current_url)
        try:
            new_urls = find_links_on_page(current_url)
            for url in new_urls:
                url_domain = urlparse(url).netloc
                if ALLOW_SUBDOMAIN:
                    url_domain = url_domain.split('.', 1)[1]
                if url not in visited_urls and url_domain == start_domain and (max_depth == -1 or current_depth < max_depth):
                    urls_to_visit.append((urldefrag(url)[0], current_depth + 1))
        except Exception as err:
            print(f"Error: couldn't scrape {current_url}, {err}")
    return visited_urls

if __name__ == "__main__":
    crawled_urls = crawl_website(WEBSITE_URL)
    print("\n".join(crawled_urls))

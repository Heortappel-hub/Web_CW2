import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE_URL = "https://quotes.toscrape.com/"


def crawl():
    frontier = [BASE_URL]      # URLs waiting to be crawled (BFS queue)
    visited = set()            # Prevent revisiting the same page
    pages = {}                 # Store crawled page text
    first_request = True

    while frontier:
        current_url = frontier.pop(0)   # Get next URL from frontier

        if current_url in visited:
            continue
        if urlparse(current_url).netloc != urlparse(BASE_URL).netloc:   # Skip external links, netloc is the domain part of the URL in urlparse
            continue                    

        if not first_request:
            time.sleep(6)               # Respect politeness window
        first_request = False

        print(f"Crawling: {current_url}")

        try:
            response = requests.get(current_url, timeout=10)
            response.raise_for_status()
            html = response.text
        except requests.RequestException as e:
            print(f"  Error: {e}")
            visited.add(current_url)
            continue

        visited.add(current_url)

        soup = BeautifulSoup(html, "html.parser")
        pages[current_url] = soup.get_text(separator=" ", strip=True)

        # Discover hyperlinks and add unseen pages to frontier
        for a in soup.find_all("a", href=True):
            link = urljoin(current_url, a["href"]).split("#")[0]

            if link not in visited:
                frontier.append(link)

    return pages

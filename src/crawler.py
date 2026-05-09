import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://quotes.toscrape.com/"


def fetch_page(url):
    """Send HTTP request and get page HTML content"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def crawl():
    pages = {}                      # 1. Create an empty dictionary to store all crawled pages
    current_url = BASE_URL          # 2. Start from the homepage
    first_request = True            # 3. Flag to control sleep interval

    while current_url:
        # 4. Polite crawling: wait 6 seconds before each request after the first one
        if not first_request:
            time.sleep(6)
        first_request = False

        print(f"Crawling: {current_url}")

        # 5. Get page HTML
        html = fetch_page(current_url)
        if html is None:
            print(f"Failed to fetch {current_url}.")
            break

        # 6. Parse HTML content
        soup = BeautifulSoup(html, "html.parser")

        # 7. Extract indexable text and store in the dictionary
        page_text = soup.get_text(separator=" ", strip=True)
        pages[current_url] = page_text

        # 8. Find the next page link
        next_li = soup.find("li", class_="next")
        if next_li:
            next_link = next_li.find("a")["href"]
            current_url = urljoin(BASE_URL, next_link)
        else:
            current_url = None      

    return pages                    # 9. Return the complete dictionary of pages
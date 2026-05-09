import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://quotes.toscrape.com/"
current_url = BASE_URL

def fetch_page(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

while current_url:

    print(f"Crawling: {current_url}")

    html = fetch_page(current_url)

    soup = BeautifulSoup(html, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        print(text)

    next_exists = soup.find("li", class_="next")

    if next_exists:
        next_link = next_exists.find("a")["href"]
        current_url = urljoin(BASE_URL, next_link)
    else:
        current_url = None

    time.sleep(6)
    
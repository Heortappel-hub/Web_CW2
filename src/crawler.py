import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://quotes.toscrape.com/"

def fetch_page(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

html = fetch_page(BASE_URL)

soup = BeautifulSoup(html, "html.parser")

quotes = soup.find_all("div", class_="quote")
for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    print(text)

next_button = soup.find("li", class_="next")
next_link = next_button.find("a")["href"]
full_url = urljoin(BASE_URL, next_link)
print(full_url)
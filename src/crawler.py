import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com/"

def fetch_page(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

html = fetch_page(BASE_URL)
print(html[:500])
"""Unit tests for the crawler module"""
import unittest
from unittest.mock import patch, MagicMock

# Add the src directory to the path for importing
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from crawler import fetch_page, crawl


class TestFetchPage(unittest.TestCase):
    """Test the fetch_page function"""

    @patch('crawler.requests.get')
    def test_fetch_page_success(self, mock_get):
        """Should return the page HTML on success"""
        # Mock a successful response from requests.get
        mock_response = MagicMock()
        mock_response.text = "<html>hello</html>"
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = fetch_page("https://example.com")
        self.assertEqual(result, "<html>hello</html>")

    @patch('crawler.requests.get')
    def test_fetch_page_failure(self, mock_get):
        """Should return None when the request fails"""
        import requests
        mock_get.side_effect = requests.RequestException("boom")

        result = fetch_page("https://example.com")
        self.assertIsNone(result)


class TestCrawl(unittest.TestCase):
    """Test the crawl function"""

    @patch('crawler.time.sleep')          # Skip sleep to speed up tests
    @patch('crawler.fetch_page')
    def test_crawl_returns_dict(self, mock_fetch, mock_sleep):
        """crawl should return a dictionary type"""
        # Mock a simple single-page website
        mock_fetch.return_value = "<html><body>hello world</body></html>"

        result = crawl()
        self.assertIsInstance(result, dict)

    @patch('crawler.time.sleep')
    @patch('crawler.fetch_page')
    def test_crawl_handles_fetch_failure(self, mock_fetch, mock_sleep):
        """Should exit gracefully without crashing if fetch fails"""
        mock_fetch.return_value = None

        result = crawl()
        self.assertEqual(result, {})  # No data crawled, but no errors


if __name__ == "__main__":
    unittest.main()
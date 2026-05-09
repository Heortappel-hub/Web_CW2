"""Unit tests for the crawler module"""
import unittest
from unittest.mock import patch, MagicMock

# Add src directory to import path
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from crawler import crawl


class TestCrawl(unittest.TestCase):

    @patch('crawler.time.sleep')
    @patch('crawler.requests.get')
    def test_crawl_returns_pages(self, mock_get, mock_sleep):
        """Should successfully crawl and return a non-empty dict"""
        mock_response = MagicMock()
        mock_response.text = "<html><body>hello world</body></html>"
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = crawl()
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 1)
        self.assertIn("https://quotes.toscrape.com/", result)

    @patch('crawler.time.sleep')
    @patch('crawler.requests.get')
    def test_crawl_follows_internal_links(self, mock_get, mock_sleep):
        """BFS should follow links to discover new pages"""
        # Home page links to /page/2/, page 2 has no further links
        responses = [
            MagicMock(text='<html><body><a href="/page/2/">Next</a></body></html>'),
            MagicMock(text='<html><body><p>page 2</p></body></html>'),
        ]
        for r in responses:
            r.raise_for_status = MagicMock()
        mock_get.side_effect = responses

        result = crawl()
        # Both pages should be crawled
        self.assertEqual(len(result), 2)
        self.assertIn("https://quotes.toscrape.com/", result)
        self.assertIn("https://quotes.toscrape.com/page/2/", result)


if __name__ == "__main__":
    unittest.main()
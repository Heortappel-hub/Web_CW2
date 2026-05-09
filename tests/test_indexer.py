"""Unit tests for the indexer module"""
import unittest

# Add src directory to import path
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from indexer import build_index


class TestIndexer(unittest.TestCase):

    def test_basic_index(self):
        """Should build a correct inverted index from a small mock dataset"""
        fake_pages = {
            "url1": "good morning good",
            "url2": "good night"
        }
        index = build_index(fake_pages)

        # 'good' appears in both URLs
        self.assertIn("good", index)
        self.assertEqual(set(index["good"].keys()), {"url1", "url2"})

        # In url1, 'good' appears at positions 0 and 2
        self.assertEqual(index["good"]["url1"], [0, 2])
        # In url2, 'good' appears at position 0
        self.assertEqual(index["good"]["url2"], [0])

        # 'morning' only appears in url1 at position 1
        self.assertEqual(index["morning"], {"url1": [1]})

        # 'night' only appears in url2 at position 1
        self.assertEqual(index["night"], {"url2": [1]})

    def test_case_insensitive(self):
        """Search should be case insensitive — 'Good' and 'good' are the same word"""
        fake_pages = {
            "url1": "Good GOOD good"
        }
        index = build_index(fake_pages)

        # All three should be indexed under lowercase 'good'
        self.assertIn("good", index)
        self.assertNotIn("Good", index)
        self.assertNotIn("GOOD", index)
        self.assertEqual(index["good"]["url1"], [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
"""Unit tests for the search module"""
import unittest
import os
import tempfile
import io
from contextlib import redirect_stdout

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from search import save_index, load_index, print_word, find_pages


class TestStorage(unittest.TestCase):
    """Test save/load round-trip"""

    def test_save_and_load_roundtrip(self):
        original = {
            "good": {"url1": [0, 2], "url2": [0]},
            "morning": {"url1": [1]},
        }
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as tmp:
            tmp_path = tmp.name
        try:
            save_index(original, tmp_path)
            loaded = load_index(tmp_path)
            self.assertEqual(loaded, original)
        finally:
            os.remove(tmp_path)


class TestFind(unittest.TestCase):
    """Test the find_pages logic (multi-word intersection)"""

    def setUp(self):
        # Fake index for all tests in this class
        self.index = {
            "good":    {"url1": [0], "url2": [0], "url3": [0]},
            "morning": {"url1": [1]},
            "friends": {"url2": [1], "url3": [1]},
        }

    def _capture(self, func, *args):
        """Run func(*args) and capture printed output as a string"""
        buf = io.StringIO()
        with redirect_stdout(buf):
            func(*args)
        return buf.getvalue()

    def test_find_single_word(self):
        output = self._capture(find_pages, self.index, ["good"])
        # All three pages contain "good"
        self.assertIn("url1", output)
        self.assertIn("url2", output)
        self.assertIn("url3", output)

    def test_find_multiple_words_intersection(self):
        """find 'good friends' should return only pages with BOTH words"""
        output = self._capture(find_pages, self.index, ["good", "friends"])
        # url2 and url3 have both; url1 only has 'good'
        self.assertNotIn("url1", output)
        self.assertIn("url2", output)
        self.assertIn("url3", output)

    def test_find_missing_word(self):
        """find with a word not in the index should report none found"""
        output = self._capture(find_pages, self.index, ["xyzzy"])
        self.assertIn("not in the index", output)


if __name__ == "__main__":
    unittest.main()
import unittest
from llmchain.core.text_splitter import TextSplitter

class TestTextSplitter(unittest.TestCase):
    def test_split(self):
        splitter = TextSplitter()
        text = "a\nb\nc"
        parts = splitter.split(text)
        self.assertEqual(parts, ["a", "b", "c"])

if __name__ == "__main__":
    unittest.main()

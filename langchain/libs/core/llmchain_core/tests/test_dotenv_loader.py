"""
llmchain/tests/test_dotenv_loader.py

Unit tests for the DotenvLoader class.
"""
import unittest
import os
from llmchain_core.dotenv_loader import DotenvLoader

class TestDotenvLoader(unittest.TestCase):
    def setUp(self):
        self.env_file = ".test_env"
        with open(self.env_file, "w") as f:
            f.write("FOO=bar\n# Comment line\nBAZ=qux\nINVALIDLINE\n")
        # Clean up any pre-existing env vars
        for key in ["FOO", "BAZ"]:
            if key in os.environ:
                del os.environ[key]

    def tearDown(self):
        if os.path.exists(self.env_file):
            os.remove(self.env_file)
        for key in ["FOO", "BAZ"]:
            if key in os.environ:
                del os.environ[key]

    def test_load(self):
        loader = DotenvLoader(filepath=self.env_file)
        loader.load()
        self.assertEqual(os.environ.get("FOO"), "bar")
        self.assertEqual(os.environ.get("BAZ"), "qux")
        self.assertIsNone(os.environ.get("INVALIDLINE"))

    def test_missing_file(self):
        loader = DotenvLoader(filepath="nonexistent.env")
        loader.load()  # Should not raise

if __name__ == "__main__":
    unittest.main()

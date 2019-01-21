import sys
sys.path.append("..")
from tech_questions import ExpiringDict
import unittest

class TestStringAdder(unittest.TestCase):
    def test_base(self):
        cache = ExpiringDict(cache_len=10, max_age=10)
        cache["key"] = "val"
        self.assertEqual(cache.get("key"), "val")

if __name__ == "__main__":
    unittest.main()

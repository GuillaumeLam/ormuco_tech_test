import sys
sys.path.append("..")
from tech_questions import string_num_cmp
import unittest

class TestStringAdder(unittest.TestCase):
    def test_gt(self):
        self.assertEqual(string_num_cmp("2.1", "1.8"), -1)

    def test_lt(self):
        self.assertEqual(string_num_cmp("5.7","7"), 1)

    def test_equal(self):
        self.assertEqual(string_num_cmp("0.0","0.0"), 0)

    def test_empty(self):
        self.assertEqual(string_num_cmp("",""), 2)

    def test_char(self):
        self.assertEqual(string_num_cmp("sf","efg"), 2)

    def test_int(self):
        self.assertEqual(string_num_cmp("5", "10"), 1)

    def test_one_char(self):
        self.assertEqual(string_num_cmp("5","orm"), 2)

    def test_no_str(self):
        self.assertEqual(string_num_cmp(5,"5"), 0)

    def test_list(self):
        self.assertEqual(string_num_cmp([2,4],"3.5"), 2)


if __name__ == "__main__":
    unittest.main()

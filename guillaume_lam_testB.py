import unittest

# function return a -1 if num1 is bigger,
# 0 if both are equal,
# 1 if num2 is bigger,
# and finally a 2 if one stirng is not a number
def string_num_cmp(str_num1: str, str_num2: str)-> int:
    try:
        num1 = float(str_num1)
        num2 = float(str_num2)

        if num1 > num2:
            return -1
        elif num1 < num2:
            return 1
        else:
            return 0
    except (ValueError, TypeError):
        return 2

#
#

# tests for the function abover, would put in a seperate file but don't want
# to complicate things for the technical test
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

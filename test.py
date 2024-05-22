import unittest
from source import add

class TestCalc(unittest.TestCase):

    def test_empty_calc(self):
        self.assertEqual(add(""), 0)

    def test_single_num_calc(self):
        self.assertEqual(add("1"), 1)

    def test_multi_num_calc(self):
        self.assertEqual(add("1,2"), 3)

    def test_ignore_calc(self):
        self.assertEqual(add("1000,2"), 2)

    def test_new_line_calc(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimet_calc(self):
        self.assertEqual(add("//;\n1;2"), 3)
    
    def test_negative_num_calc(self):
        with self.assertRaises(ValueError) as c:
            add("1,-2")
        self.assertEqual(str(c.exception), "negative numbers not allowed -2")


unittest.main()

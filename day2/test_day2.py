import unittest

from day2 import find_checksum
from day2 import find_similar_strings


class Test_day_modules(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test.txt'

    def test_find_checksum(self):
        expected = 1
        mylines = ["aaabbbcceeffgz"]
        self.assertEqual(expected, find_checksum(mylines))

    def test_find_similar_Strings(self):
        expected = ("aaaaaaaaaa", "aaaaaaaaab")
        mylines = ["aaaaaaaaab", "aaaaaaaaaa", "dkoskdkdakr"]
        self.assertEqual(expected, find_similar_strings(mylines))


if __name__ == '__main__':
    unittest.main()

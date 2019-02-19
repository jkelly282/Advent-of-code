import unittest

from day2 import find_checksum, find_similar_strings, remove_duplicates


class Test_day_modules(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test.txt'

    def test_find_checksum(self):
        expected = 1
        mylines = ["aaabbbcceeffgz"]
        self.assertEqual(expected, find_checksum(mylines))

    def test_find_checksum_fail(self):
        expected = 1
        mylines = ["214152452423413412"]
        self.assertNotEqual(expected, find_checksum(mylines))

    def test_find_checksum_type_error(self):
        expected = 1
        mylines = ("hello")
        self.assertRaises(TypeError, find_checksum(mylines), self.test_file)

    def test_find_similar_Strings(self):
        expected = ("aaaaaaaaaa", "aaaaaaaaab")
        mylines = ["aaaaaaaaab", "aaaaaaaaaa", "dkoskdkdakr"]
        self.assertEqual(expected, find_similar_strings(mylines))

    def test_remove_duplicates(self):
        expected = ['a'] * 9
        test = ("aaaaaaaaaa", "aaaaaaaaab")
        self.assertEqual(expected, remove_duplicates(test))


if __name__ == '__main__':
    unittest.main()

import unittest

from day2 import find_checksum, find_similar_strings, remove_duplicates


class TestDayModules(unittest.TestCase):

    def test_find_checksum(self):
        expected = 1
        mylines = ["aaabbbcceeffgz"]
        self.assertEqual(expected, find_checksum(mylines))

    def test_find_checksum_fail(self):
        expected = 1
        mylines = ["214152452423413412"]
        self.assertNotEqual(expected, find_checksum(mylines))

    def test_find_checksum_type_error(self):
        mylines = (22)
        self.assertRaises(TypeError, find_checksum, mylines)

    def test_find_similar_Strings(self):
        expected = ("aaaaaaaaaa", "aaaaaaaaab")
        mylines = ["aaaaaaaaab", "aaaaaaaaaa", "dkoskdkdakr"]
        self.assertEqual(expected, find_similar_strings(mylines))

    def test_find_similar_strings_fail(self):
        expected = ("aaaaaaaaaa", "aaaaaaaaab")
        mylines = ("I wanna be the very best like no-one ever was ")
        self.assertNotEqual(expected, find_similar_strings(mylines))

    def test_find_similar_strings_fail_empty(self):
        expected = ("aaaaaaaaaa", "aaaaaaaaab")
        mylines = ()
        self.assertNotEqual(expected, find_similar_strings(mylines))

    def test_remove_duplicates(self):
        expected = ['a'] * 9
        test = ("aaaaaaaaaa", "aaaaaaaaab")
        self.assertEqual(expected, remove_duplicates(test))

    def remove_duplicates_fail(self):
        expected = ['a'] * 9
        test = ("To catch them is my real goal, to train them is my cause")
        self.assertNotEqual(expected, find_similar_strings(test))


if __name__ == '__main__':
    unittest.main()

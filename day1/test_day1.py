import unittest

from pyfakefs.fake_filesystem_unittest import Patcher

from day1 import open_file
from day1_extra import find_duplicate


class TestOpenFile(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test.txt'

    def test_open_file_success(self):
        expected = [1, -2, 5]
        with Patcher() as patch:
            patch.fs.create_file(self.test_file, contents="+1\n-2\n+5\n")
            self.assertEqual(expected, open_file(self.test_file))

    def test_open_file_fail(self):
        expected = [1, 3, 5]
        with Patcher() as patch:
            patch.fs.create_file(self.test_file, contents="+1\n-2\n+5\n")
            self.assertNotEqual(expected, open_file(self.test_file))

    def test_open_file_throws_exception(self):
        with Patcher() as patch:
            patch.fs.create_file(self.test_file, contents="This should really fail")
            self.assertRaises(ValueError, open_file, self.test_file)

    def test_find_duplicate(self):
        expected = 2
        input_list = [1, 1, 2, 1, -3]
        self.assertEqual(expected, find_duplicate(input_list))

if __name__ == '__main__':
    unittest.main()

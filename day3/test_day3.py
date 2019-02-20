import unittest

import day3


class TestDay3(unittest.TestCase):
    def test_open_file(self):
        self.assertEqual('x', day3.open_file("myfile"))

    def test_parse_claims(self):
        expected = [['1', '2', '3', '4']]
        mylines = ["#1 @ 1,2: 3x4"]
        self.assertEqual(expected, day3.parse_claims(mylines))

    def test_parse_claims_fail(self):
        expected = [['1', '2', '3', '4']]
        mylines = ["1234"]
        self.assertNotEqual(expected, day3.parse_claims(mylines))

    def test_parse_claims_type(self):
        mylines = 43770
        self.assertRaises(TypeError, day3.parse_claims, mylines)

    def test_parse_claims_empty(self):
        expected = [['1', '2', '3', '4']]
        mylines = [""]
        self.assertNotEqual(expected, day3.parse_claims(mylines))


if __name__ == '__main__':
    unittest.main()

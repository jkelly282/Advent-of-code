import unittest

import day3


class TestDay3(unittest.TestCase):
    def test_parse_claims(self):
        expected = [['1', '1', '2', '3', '4']]
        mylines = ["#1 @ 1,2: 3x4"]
        self.assertEqual(expected, day3.parse_claims(mylines))

    def test_parse_claims_fail(self):
        expected = [['1', '2', '3', '4']]
        mylines = ["1234"]
        self.assertNotEqual(expected, day3.parse_claims(mylines))

    def test_parse_claims_type(self):
        mylines = "Wait a minute Link, don't leave the cave, where do you think you're going?! " \
                  "This is a great chance to ###### a ####### as you're ####### "
        self.assertRaisesRegex(TypeError, r"mylines", day3.parse_claims, mylines)

    def test_parse_claims_empty(self):
        mylines = []
        self.assertRaises(ValueError, day3.parse_claims, mylines)

    def test_parse_fabric_list(self):
        expected = 4
        claims = [[1, 1, 3, 4, 4], [2, 3, 1, 4, 4]]
        self.assertEqual(expected, day3.parse_fabric_list(claims, 8))

    def test_parse_fabric_list_string(self):
        claims = [[1, 1, 3, 4, 4], [2, 3, 1, 4, 4]]
        self.assertRaises(TypeError, day3.parse_fabric_list, claims, "8")

    def test_parse_fabric_list_size_dosent_matter(self):
        expected = 4
        claims = [[1, 1, 3, 4, 4], [2, 3, 1, 4, 4]]
        self.assertEqual(expected, day3.parse_fabric_list(claims, 1000))

if __name__ == '__main__':
    unittest.main()

"""
test fizzbuzz

"""

import unittest
import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_num_3_and_5(self):
        self.assertEqual(fizzbuzz.FizzBuzz(15), 'FizzBuzz')

    def test_num_3(self):
        self.assertEqual(fizzbuzz.FizzBuzz(3), 'Fizz')

    def test_num_5(self):
        self.assertEqual(fizzbuzz.FizzBuzz(5), 'Buzz')

    def test_num_other(self):
        self.assertEqual(fizzbuzz.FizzBuzz(2), 2)


if __name__ == '__main__':
    unittest.main()

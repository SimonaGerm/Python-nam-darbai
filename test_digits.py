import unittest

from task_class4 import count_digits, count_zeros


class TestDigits(unittest.TestCase):

    def test_one_digit(self):
        self.assertEqual(count_digits(5), 1, msg='neteisingai')

    def test_two_digits(self):
        self.assertEqual(count_digits(55), 2)

    def test_many_digits(self):
        self.assertEqual(count_digits(111111111111), 12)

    def test_false_input(self):
        with self.assertRaises(ValueError):
            count_digits('aaaaabs')


class TestZeroes(unittest.TestCase):

    def test_no_zeroes(self):
        self.assertEqual(count_zeros(123), 0)

    def test_one_zero(self):
        self.assertEqual(count_zeros(10), 1)

    def test_many_zeroes(self):
        self.assertEqual(count_zeros(100000000), 8)

    def test_only_zeroes_as_string(self):
        self.assertEqual(count_zeros('000'), 3)

    def test_only_zeroes_as_int(self):
        self.assertEqual(count_zeros(000), 1)


if __name__ == '__main__':

    unittest.main()
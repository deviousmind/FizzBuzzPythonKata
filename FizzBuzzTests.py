import unittest
from FizzBuzzModule import FizzBuzz

class FizzBuzzTests(unittest.TestCase):
    def test_get_answer_1(self):
        result = FizzBuzz.get_answer(1)
        expected = '1'
        self.assertEqual(result, expected)

    def test_get_answer_2(self):
        result = FizzBuzz.get_answer(2)
        expected = '2'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

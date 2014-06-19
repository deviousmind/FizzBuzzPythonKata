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

    def test_get_answer_3(self):
        result = FizzBuzz.get_answer(3)
        expected = 'fizz'
        self.assertEqual(result, expected)

    def test_get_answer_5(self):
        result = FizzBuzz.get_answer(5)
        expected = 'buzz'
        self.assertEqual(result, expected)

    def test_get_answer_6(self):
        result = FizzBuzz.get_answer(6)
        expected = 'fizz'
        self.assertEqual(result, expected)

    def test_get_answer_9(self):
        result = FizzBuzz.get_answer(9)
        expected = 'fizz'
        self.assertEqual(result, expected)

    def test_get_answer_10(self):
        result = FizzBuzz.get_answer(10)
        expected = 'buzz'
        self.assertEqual(result, expected)

    def test_get_answer_20(self):
        result = FizzBuzz.get_answer(20)
        expected = 'buzz'
        self.assertEqual(result, expected)

    def test_get_answer_15(self):
        result = FizzBuzz.get_answer(15)
        expected = 'fizzbuzz'
        self.assertEqual(result, expected)

    def test_get_answer_30(self):
        result = FizzBuzz.get_answer(30)
        expected = 'fizzbuzz'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

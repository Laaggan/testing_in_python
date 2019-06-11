import unittest
from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        '''
        This test checks if sum can add a list of integers
        '''
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6, 'Should be 6!')

    def test_list_fractions(self):
        '''
        This test checks if fractions can be added by the function sum
        '''
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 4)]
        result = sum(data)
        self.assertEqual(result, 1, 'Should be 1!')

    def test_bad_type(self):
        '''
        This test checks that an error is thrown when sum is given a string
        '''
        data = 'banana'
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == 'main':
    unittest.main()
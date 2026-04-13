import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): 
        self.assertEqual(add(2, 3), 5)      
        self.assertEqual(add(-1, 1), 0)    
        self.assertEqual(add(0, 0), 0)  

    def test_subtract(self): 
        self.assertEqual(subtract(5, 3), 2)    
        self.assertEqual(subtract(0, 5), -5)   
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(-3, 7), -21)
        self.assertEqual(multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(divide(6, 30), 5)
        self.assertEqual(divide(-5, 20), -4)
        self.assertEqual(divide(2, 1), 0.5)

    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(5, 25), 2)    
        self.assertEqual(logarithm(10, 100), 2) 
        self.assertEqual(logarithm(2, 8), 3)    

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 7), math.sqrt(74))
        self.assertEqual(hypotenuse(10, 5), math.sqrt(125))

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(127.5), 127.5 ** 0.5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
from calculator import *
import unittest

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(10, 3), 7)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-3, -3), 0)
    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(4,3), 12)
        self.assertEqual(mul(-2, 12), -24)
        self.assertEqual(mul(0, 6), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(3, 9), 3)
        self.assertEqual(div(4, 20), 5)


    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(3, 27), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(-2, 8)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(10, -4)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
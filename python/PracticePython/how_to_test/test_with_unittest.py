import unittest # 1. Import unittest from standard library.

# 2. Inherit from unittest.TestCase
class TestSum(unittest.TestCase):
    # 3. Convert test functions into methods by adding self as the argument
    def test_sum(self):
        # 4. change the assertion to self.assertEqual()
        self.assertEqual(sum([1,2,3]), 6, "Should be 6.")
    
    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,2)), 6, "Shold be 6.")


if __name__ == '__main__':
    unittest.main() #5. Change the command-line entry point.


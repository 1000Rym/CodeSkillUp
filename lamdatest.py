
# This project created for check Lamda function and Test Driven Develop mechanism


import unittest

class TddTest(unittest.TestCase):

    def testAdd(self):
        plus = lambda x,y : x + y
        result = plus(1+2)
        self.assertEqual(result, 3)

    def testAdd(self):
        minus = lambda x,y : x -y
        result = minus(3,1)
        self.assertEqual(result, 2)



if __name__ == "__main__":
    unittest.main();
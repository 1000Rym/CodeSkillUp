import unittest
from ..implementation import ice_cream_maker

class TestIceCreamMaker(unittest.TestCase):
    def test_function1(self):
        rows, columns = 4, 5
        graph = [[0,0,1,1,0],
                 [0,0,0,1,1],
                 [1,1,1,1,1],
                 [0,0,0,0,0]
                ]
        self.assertEqual(ice_cream_maker.find_icecream_blocks(rows, columns, graph),3)
        
    def test_function2(self):
        rows, columns = 15,14
        graph = [
            [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
            [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
            [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
            [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
            [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
            [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
            [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
            [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
        ]
        self.assertEqual(ice_cream_maker.find_icecream_blocks(rows, columns, graph),8)
        
    
    
if __name__ == '__main__':
    unittest.main()
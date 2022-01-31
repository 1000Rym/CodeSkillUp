import unittest
from ..search import escape_maze

class TestEscapeMaze(unittest.TestCase):
    def test_escape_maze(self):
        N, M = 5, 6
        map_info = [[1, 0, 1, 0, 1, 0], 
                    [1, 1, 1, 1, 1, 1], 
                    [0, 0, 0, 0, 0, 1], 
                    [1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1]]
        
        self.assertEqual(escape_maze.escape_maze(N,M,map_info), 10)
        

if __name__ == '__main__':
    unittest.main()
import math
import unittest
import graph_data
from pathing import bfs, dfs, generate_random_path, get_dfs_path 

class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
        
    def setUp(self):
        self.graph = graph_data.graph_data[1]

    def test_generate_random_path(self):
        start = 0
        end = len(self.graph) - 1
        target = 2  
        
        path = generate_random_path(self.graph, start, end, target)  

        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], end)

    def test_generate_dfs_path(self):
        start = 0
        end = len(self.graph) - 1
        
        path = dfs(self.graph, start, end, visited=[], currpath=[])

        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], end)
    
    def test_generate_bfs_path(self):
        start = 0
        end = len(self.graph) - 1
        
        path = bfs(self.graph, start, end)

        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], end)

if __name__ == '__main__':
    unittest.main()



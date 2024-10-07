import math
import unittest
from pathing import generate_random_path 

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


if __name__ == '__main__':
    unittest.main()

def setUp(self):
        # Test graph
        self.graph = [
            [(0, 0), [1, 2]],    
            [(1, 1), [0, 3]],    
            [(2, 2), [0, 3, 4]], 
            [(3, 3), [1, 2]],   
            [(4, 4), [2]],       
        ]
    
def test_generate_random_path(self):
        start = 0
        end = 4
        
        path = generate_random_path(self.graph, start, end)
        self.assertTrue(path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], end)
        self.assertIn(end, path)
        
        for node in path:
            self.assertIn(node, range(len(self.graph)))

def test_edge_case_no_path(self):
        disconnected_graph = [
            [(0, 0), [1]],
            [(1, 1), [0]],
            [(2, 2), []], 
        ]
        start = 0
        end = 2
        path = generate_random_path(disconnected_graph, start, end)
        
        self.assertEqual(path, [])

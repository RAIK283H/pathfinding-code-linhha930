import math
import unittest
import graph_data
from pathing import bfs, dfs, generate_random_path, get_dfs_path
from permutation import find_largest_mobile_integer, generate_permutations, is_hamiltonian, sjt_hamiltonian_cycles 

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

    def test_find_largest_mobile_integer(self):
        permutations = [1, 3, 2]
        directions = [-1, -1, 1] 
        
        largest_index = find_largest_mobile_integer(permutations, directions)
        
        self.assertEqual(largest_index, 1)

        permutations = [3, 2, 1]
        directions = [-1, -1, -1]  # No mobile integer
        largest_index = find_largest_mobile_integer(permutations, directions)
        self.assertEqual(largest_index, -1)

    def test_find_largest_mobile_integer_edge_case(self):
        permutations = [1, 2, 3, 4]
        directions = [1, 1, 1, -1]  # The last element (4) can move left
        largest_index = find_largest_mobile_integer(permutations, directions)
        self.assertEqual(largest_index, 3)  # 4 is the largest mobile integer at index 3

    def test_is_hamiltonian_valid(self):
        graph = [
            [(0, 0), [1]],    
            [(1, 1), [0, 2]], 
            [(2, 2), [1, 3]], 
            [(3, 3), [2, 0]]  
        ]

        res = is_hamiltonian(graph, [1, 2])
        self.assertTrue(res)  
    
    def test_is_hamiltonian_invalid(self):
        graph = [
            [(0, 0), [1]],    
            [(1, 1), [0, 2]], 
            [(2, 2), [1, 3]], 
            [(3, 3), [2, 0]]  
        ]

        res = is_hamiltonian(graph, [1, 2, 3])
        self.assertFalse(res)  

    def test_generate_permutations(self):
        nodes = [1, 2, 3]
        
        expected_permutations = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 2, 1],
            [3, 1, 2],
        ]

        actual_permutations = generate_permutations(nodes)
        self.assertEqual(sorted(actual_permutations), sorted(expected_permutations))

    def test_sjt_hamiltonian_cycles(self):
        graph = [
            [(0, 0), [1]],    
            [(1, 1), [0, 2]], 
            [(2, 2), [1, 3]], 
            [(3, 3), [2, 0]]  
        ]

        expected_cycles = [[1, 2], [2, 1]]
        result = sjt_hamiltonian_cycles(graph)
        self.assertEqual(result, expected_cycles)

if __name__ == '__main__':
    unittest.main()



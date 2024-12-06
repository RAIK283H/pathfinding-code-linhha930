import math
import unittest
from f_w import adj_list_to_matrix, build_path, floyd_warshall

class TestPathFinding(unittest.TestCase):

    def setUp(self):
        # Test graph 1
        self.graph1 = [
            ((0, 0), [1, 2]),
            ((1, 0), [0, 2, 3]),
            ((0, 1), [0, 1]),
            ((1, 1), [1])
        ]
        
        # Test graph 2
        self.graph2 = [
            ((0, 0), [1]),
            ((1, 0), [2]),
            ((2, 0), [3]),
            ((3, 0), [])
        ]

    def test_build_path(self):
        distance, parent = floyd_warshall(self.graph1)
        path = build_path(parent, 0, 3)
        self.assertEqual(path, [0, 1, 3]) 

        distance, parent = floyd_warshall(self.graph2)
        path = build_path(parent, 0, 3)
        self.assertEqual(path, [0, 1, 2, 3])  

    def test_floyd_warshall_graph1(self):
        distance, parent = floyd_warshall(self.graph1)

        expected_distance = [
            [2.0, 1.0, 1.0, 2.0],
            [1.0, 2.0, 1.4142135623730951, 1.0],
            [1.0, 1.4142135623730951, 2.0, 2.414213562373095],
            [2.0, 1.0, 2.414213562373095, 2.0]
        ]

        for i in range(len(expected_distance)):
            for j in range(len(expected_distance)):
                self.assertAlmostEqual(
                    distance[i][j],
                    expected_distance[i][j],
                    places=5,
                    msg=f"Distance mismatch at ({i}, {j}): {distance[i][j]} != {expected_distance[i][j]}"
                )

    def test_floyd_warshall_graph2(self):
        distance, parent = floyd_warshall(self.graph2)

        expected_distance = [
            [math.inf, 1.0, 2.0, 3.0],
            [math.inf, math.inf, 1.0, 2.0],
            [math.inf, math.inf, math.inf, 1.0],
            [math.inf, math.inf, math.inf, math.inf]
        ]

        for i in range(len(expected_distance)):
            for j in range(len(expected_distance)):
                self.assertAlmostEqual(
                    distance[i][j],
                    expected_distance[i][j],
                    places=5,
                    msg=f"Distance mismatch at ({i}, {j}): {distance[i][j]} != {expected_distance[i][j]}"
                )
    
    def test_adj_list_to_matrix_graph1(self):
        matrix = adj_list_to_matrix(self.graph1)

        expected_matrix = [
            [math.inf, 1.0, 1.0, math.inf],
            [1.0, math.inf, 1.4142135623730951, 1.0],
            [1.0, 1.4142135623730951, math.inf, math.inf],
            [math.inf, 1.0, math.inf, math.inf]
        ]

        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix[i])):
                self.assertAlmostEqual(
                    matrix[i][j],
                    expected_matrix[i][j],
                    places=5,
                    msg=f"Matrix mismatch at ({i}, {j}): {matrix[i][j]} != {expected_matrix[i][j]}"
                )

    def test_adj_list_to_matrix_graph2(self):
        matrix = adj_list_to_matrix(self.graph2)

        expected_matrix = [
            [math.inf, 1.0, math.inf, math.inf],
            [math.inf, math.inf, 1.0, math.inf],
            [math.inf, math.inf, math.inf, 1.0],
            [math.inf, math.inf, math.inf, math.inf]
        ]

        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix[i])):
                self.assertAlmostEqual(
                    matrix[i][j],
                    expected_matrix[i][j],
                    places=5,
                    msg=f"Matrix mismatch at ({i}, {j}): {matrix[i][j]} != {expected_matrix[i][j]}"
                )

        
if __name__ == '__main__':
    unittest.main()
    
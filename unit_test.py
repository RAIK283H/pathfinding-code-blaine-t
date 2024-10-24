import math
import unittest

import global_game_data
import graph_data
from pathing import get_bfs_path, get_dfs_path

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

    def test_bfs_path_working(self):
        graph_index = 0
        target_node = 5

        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        graph_data.graph_data = {
            graph_index: [
                (0, [1, 2]),
                (1, [3]),
                (2, [3, 4]),
                (3, [5]),
                (4, [5]),
                (5, [6, 7]),
                (6, [8]),
                (7, [8]),
                (8, [9]),
                (9, [])
            ]
        }
        expected_path = [1, 3, 5, 6, 8, 9]
        bfs_path = get_bfs_path()
        self.assertEqual(bfs_path, expected_path)

    def test_bfs_failing(self):
        graph_index = 0
        target_node = 5

        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        graph_data.graph_data = {
            graph_index: [
                (0, [1, 2]),
                (1, [3]),
                (2, [3, 4]),
                (3, []),
                (4, []),
                (5, []),
                (6, [8]),
                (7, [8]),
                (8, [9]),
                (9, [])
            ]
        }
        try:
            get_bfs_path()
        except(AssertionError):
            return
        self.fail("BFS didn't throw an assertion error")

    def test_dfs_path(self):
        graph_index = 0
        target_node = 5

        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        graph_data.graph_data = {
            graph_index: [
                (0, [1, 2]),
                (1, [3]),
                (2, [3, 4]),
                (3, [5]),
                (4, [5]),
                (5, [6, 7]),
                (6, [8]),
                (7, [8]),
                (8, [9]),
                (9, [])
            ]
        }
        expected_path = [2, 4, 5, 7, 8, 9]
        dfs_path = get_dfs_path()
        self.assertEqual(dfs_path, expected_path)

    def test_dfs_failing(self):
        graph_index = 0
        target_node = 5

        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        graph_data.graph_data = {
            graph_index: [
                (0, [1, 2]),
                (1, [3]),
                (2, [3, 4]),
                (3, []),
                (4, []),
                (5, []),
                (6, [8]),
                (7, [8]),
                (8, [9]),
                (9, [])
            ]
        }
        try:
            get_dfs_path()
        except(AssertionError):
            return
        self.fail("DFS didn't throw an assertion error")

if __name__ == '__main__':
    unittest.main()

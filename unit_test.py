import math
import unittest

import global_game_data
import graph_data
from pathing import get_bfs_path, get_dfs_path, get_dijkstra_path
from permutation import get_permutations_sjt, get_hamiltonian_cycles
from f_w import get_floyd_warshall_path


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("test".upper(), "TEST")

    def test_isupper(self):
        self.assertTrue("TEST".isupper())
        self.assertFalse("Test".isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1 / 100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value, second_value)
        self.assertAlmostEqual(first=first_value, second=second_value, delta=1e-9)
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
                (9, []),
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
                (9, []),
            ]
        }
        try:
            get_bfs_path()
        except AssertionError:
            return
        self.fail("BFS didn't throw an assertion error")

    def test_dijkstras_path_working(self):
        graph_index = 0
        target_node = 5

        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        graph_data.graph_data = {
            graph_index: [
                ((0,0), [1, 2]),
                ((1,0), [3]),
                # In an attempt to throw it off by shortest amount of nodes. DFS and BFS would take this
                ((-100,0), [9]),
                ((3,0), [5]),
                ((4,0), [5]),
                ((5,0), [6, 7]),
                ((6,0), [8]),
                ((7,0), [8]),
                ((8,0), [9]),
                ((9,0), []),
            ]
        }
        expected_path = [1, 3, 5, 6, 8, 9]
        dijkstra_path = get_dijkstra_path()
        self.assertEqual(dijkstra_path, expected_path)

    def test_dijkstras_failing(self):
        graph_index = 0
        target_node = 5

        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        graph_data.graph_data = {
            graph_index: [
                ((0,0), [1, 2]),
                ((1,0), [3]),
                ((2,0), [3, 4]),
                ((3,0), []),
                ((4,0), []),
                ((5,0), []),
                ((6,0), [8]),
                ((7,0), [8]),
                ((8,0), [9]),
                ((9,0), []),
            ]
        }
        try:
            get_dijkstra_path()
        except AssertionError:
            return
        self.fail("Dijkstra's didn't throw an assertion error")

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
                (9, []),
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
                (9, []),
            ]
        }
        try:
            get_dfs_path()
        except AssertionError:
            return
        self.fail("DFS didn't throw an assertion error")

    def test_get_permutations_sjt_4(self):
        actual_permutations = get_permutations_sjt(4)
        expected_permutations = [
            [1, 2, 3],
            [1, 3, 2],
            [3, 1, 2],
            [3, 2, 1],
            [2, 3, 1],
            [2, 1, 3],
        ]
        self.assertEqual(actual_permutations, expected_permutations)

    def test_get_permutations_sjt_5(self):
        actual_permutations = get_permutations_sjt(5)
        expected_permutations = [
            [1, 2, 3, 4],
            [1, 2, 4, 3],
            [1, 4, 2, 3],
            [4, 1, 2, 3],
            [4, 1, 3, 2],
            [1, 4, 3, 2],
            [1, 3, 4, 2],
            [1, 3, 2, 4],
            [3, 1, 2, 4],
            [3, 1, 4, 2],
            [3, 4, 1, 2],
            [4, 3, 1, 2],
            [4, 3, 2, 1],
            [3, 4, 2, 1],
            [3, 2, 4, 1],
            [3, 2, 1, 4],
            [2, 3, 1, 4],
            [2, 3, 4, 1],
            [2, 4, 3, 1],
            [4, 2, 3, 1],
            [4, 2, 1, 3],
            [2, 4, 1, 3],
            [2, 1, 4, 3],
            [2, 1, 3, 4],
        ]
        self.assertEqual(actual_permutations, expected_permutations)

    def test_get_hamiltonian_cycles_happy_path(self):
        graph = [
            [(0, 0), [1]],
            [(50, -200), [0, 2, 4]],
            [(50, -300), [1, 3]],
            [(50, -300), [2, 4]],
            [(50, -300), [3, 1, 5]],
            [(200, -500), [4]],
        ]
        actual_hamiltonian_cycles = get_hamiltonian_cycles(graph)
        expected_hamiltonian_cycles = [
            [1, 2, 3, 4],
            [4, 1, 2, 3],
            [1, 4, 3, 2],
            [3, 4, 1, 2],
            [4, 3, 2, 1],
            [3, 2, 1, 4],
            [2, 3, 4, 1],
            [2, 1, 4, 3]
        ]

        self.assertEqual(actual_hamiltonian_cycles, expected_hamiltonian_cycles)

    def test_get_hamiltonian_cycles_not_paths(self):
        graph = [
            [(0, 0), [1]],
            [(50, -200), [0, 2]],
            [(50, -300), [1, 3]],
            [(50, -300), [2, 4]],
            [(200, -500), [3]],
        ]
        actual_hamiltonian_cycles = get_hamiltonian_cycles(graph)
        expected_hamiltonian_cycles = -1
        self.assertEqual(actual_hamiltonian_cycles, expected_hamiltonian_cycles)

    def test_get_hamiltonian_cycles_unhappy_path(self):
        graph = [
            [(0, 0), [1]],
            [(50, -200), [0, 2]],
            [(50, -300), [1, 3, 4]],
            [(50, -300), [2]],
            [(50, -300), [2]],
            [(200, -500), [4]],
        ]
        actual_hamiltonian_cycles = get_hamiltonian_cycles(graph)
        expected_hamiltonian_cycles = -1
        self.assertEqual(actual_hamiltonian_cycles, expected_hamiltonian_cycles)

    def test_floyd_warshall_finds_shortest_path(self):
        graph_index = 0
        target_node = 5

        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        graph_data.graph_data = {
            graph_index: [
                ((0, 0), [1, 2]),
                ((100, 0), [3]),
                ((2, 0), [3, 4]),
                ((300, 0), [5]),
                ((4, 0), [5]),
                ((-500, 0), [6, 7]),
                ((6, 1), [8]),
                ((7, 0), [8]),
                ((8, 0), [9]),
                ((9, 0), []),
            ]
        }
        expected_path = [2, 4, 5, 7, 8, 9]
        f_w_path = get_floyd_warshall_path()
        self.assertEqual(f_w_path, expected_path)

if __name__ == "__main__":
    unittest.main()

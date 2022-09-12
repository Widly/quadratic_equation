import unittest
from copy import copy

from solver import solve


class TestSolver(unittest.TestCase):

    def test_D_is_lesser_than_zero(self):
        assert solve(1.0, 0.0, 1.0) == []

    def test_D_is_greater_than_zero(self):
        assert solve(1.0, 0.0, -1.0) == [1.0, -1.0]

    def test_D_is_zero(self):
        assert solve(1.0, 2.000001, 1.0) == [-1.0000005, -1.0000005]

    def test_a_cannot_be_zero(self):
        with self.assertRaisesRegex(ValueError, "'a' equals to zero"):
            solve(1e-6, 0.0, 0.0)

    def test_params_only_float(self):
        valid_params = [1.0, 0.0, 1.0, 1e-5]
        assert solve(*valid_params) == []

        wrong_params = [float('nan'), float('inf'), float('-inf')]
        for i in range(len(valid_params)):
            for param in wrong_params:
                params = copy(valid_params)
                params[i] = param
                with self.assertRaisesRegex(TypeError, "Params cannot be NaN or ±Inf"):
                    solve(*params)


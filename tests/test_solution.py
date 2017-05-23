from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        l = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
        result = solution(l)
        self.assertTrue(result, [1, 2, 3, 5, 6])
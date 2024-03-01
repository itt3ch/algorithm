import unittest

def robot_seeder(m, n):
    result = []
    for i in range(m):
        row_numbers = []
        for j in range(n):
            row_numbers.append(i * n + j + 1)
        if i % 2 != 0:
            row_numbers = row_numbers[::-1]
        result += row_numbers
    return result


class TestRobotSeeder(unittest.TestCase):
    def test_grid_5x5(self):
        grid = [
            [3, 4, 2, 5, 1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5],
            [3, 2, 1, 5, 4]
        ]
        expected_result = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        self.assertEqual(robot_seeder(5, 5), expected_result)

    def test_grid_2x4(self):
        grid = [
            [3, 4, 2, 5],
            [1, 2, 3, 4]
        ]
        expected_result = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(robot_seeder(2, 4), expected_result)

    def test_grid_6x6(self):
        grid = [
            [2, 3, 4, 5, 6, 12],
            [11, 10, 9, 8, 7, 13],
            [14, 15, 16, 17, 18, 24],
            [23, 22, 21, 20, 19, 25],
            [26, 27, 28, 29, 30, 36],
            [35, 34, 33, 32, 31, 37]
        ]
        expected_result = [
            1, 2, 3, 4, 5, 6, 12, 11, 10, 9, 8, 7, 13, 14, 15, 16, 17, 18, 24,
            23, 22, 21, 20, 19, 25, 26, 27, 28, 29, 30, 36, 35, 34, 33, 32, 31
        ]
        self.assertEqual(robot_seeder(6, 6), expected_result)


if __name__ == '__main__':
    unittest.main()

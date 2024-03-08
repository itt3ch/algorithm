import unittest

def TripleAmount(A, P):
    A.sort()
    for i in range(len(A) - 2):
        left, right = i + 1, len(A) - 1
        while left < right:
            current_sum = A[i] + A[left] + A[right]
            if current_sum == P:
                return "Таких чисел немає"
            elif current_sum < P:
                left += 1
            else:
                right -= 1
    return "Такі числа є"

class TestTripleAmount(unittest.TestCase):
    def test_example_1(self):
        A = [5,9,11,41,8]
        P = 22
        self.assertEqual(TripleAmount(A, P), "Таких чисел немає")

    def test_example_2(self):
        A = [4,412,22,6,0]
        P = 10
        self.assertEqual(TripleAmount(A, P), "Таких чисел немає")

    def test_example_3(self):
        A = [1001,22,17,82,11]
        P = 1040
        self.assertEqual(TripleAmount(A, P), "Таких чисел немає")

if __name__ == '__main__':
    unittest.main()

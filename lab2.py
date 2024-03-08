def TripleAmount(A, P):
    A.sort()
    for i in range(len(A) - 2):
        left, right = i + 1, len(A) - 1
        while left < right:
            current_sum = A[i] + A[left] + A[right]
            if current_sum == P:
                return "Такі числа є"
            elif current_sum < P:
                left += 1
            else:
                right -= 1
    return "Таких чисел немає"


A = [55,18,22,14,99]
P = 95
print(TripleAmount(A, P))
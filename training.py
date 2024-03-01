def robot_seeder(m, n, pumpkin_seeds):
    result = []
    for i in range(m):
        row_numbers = []
        for j in range(n):
            pumpkin_count = pumpkin_seeds[i][j]
            for _ in range(pumpkin_count):
                result.append(i * n + j + 1)
            row_numbers = row_numbers[::-1]
        result += row_numbers
    return result
pumpkin_seeds = [
    [2,1,3],
    [2,3,1],
    [4,5,6]
]
m = len(pumpkin_seeds)
n = len(pumpkin_seeds[0])
result = robot_seeder(m,n,pumpkin_seeds)
print(result)
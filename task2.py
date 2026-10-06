import random

def generate_matrix(m, n, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(n)] for _ in range(m)]

def print_matrix(matrix):
    for row in matrix:
        print(*row)

def shift_matrix(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        matrix[i] = matrix[i][-k % cols:] + matrix[i][:-k % cols]

    matrix[:] = matrix[k % rows:] + matrix[:k % rows]

matrix = generate_matrix(4, 4, 1, 10)

print("Початкова матриця:")
print_matrix(matrix)

shift_matrix(matrix, 1)

print("\nРезультат:")
print_matrix(matrix)
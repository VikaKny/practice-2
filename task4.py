import random

def generate_matrix(n, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(n)] for _ in range(n)]

def print_matrix(matrix):
    for row in matrix:
        print(*row)

def rotate_90(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

matrix = generate_matrix(4, 1, 10)

print("Початкова матриця:")
print_matrix(matrix)

rotate_90(matrix)

print("\nРезультат:")
print_matrix(matrix)
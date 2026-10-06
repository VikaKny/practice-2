import random

def generate_matrix(m, n, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(n)] for _ in range(m)]

def print_matrix(matrix):
    for row in matrix:
        print(*row)

def subtract_average(matrix):
    for row in matrix:
        average = sum(row) / len(row)

        for j in range(len(row)):
            row[j] -= average

matrix = generate_matrix(3, 4, 1, 10)

print("Початкова матриця:")
print_matrix(matrix)

subtract_average(matrix)

print("\nРезультат:")
print_matrix(matrix)
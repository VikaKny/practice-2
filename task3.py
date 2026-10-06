import random

def generate_matrix(m, n, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(n)] for _ in range(m)]

def print_matrix(matrix):
    for row in matrix:
        print(*row)

def remove_max(matrix):
    maximum = max(max(row) for row in matrix)

    rows = {i for i, row in enumerate(matrix) if maximum in row}
    cols = {j for i in rows for j in range(len(matrix[i])) if matrix[i][j] == maximum}

    return [
        [value for j, value in enumerate(row) if j not in cols]
        for i, row in enumerate(matrix)
        if i not in rows
    ]

matrix = generate_matrix(5, 5, 1, 10)

print("Початкова матриця:")
print_matrix(matrix)

matrix = remove_max(matrix)

print("\nРезультат:")
print_matrix(matrix)
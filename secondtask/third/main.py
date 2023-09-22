import random
def generate_random_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def find_and_reverse_ordered_row(matrix):
    for row in matrix:
        if all(row[i] <= row[i+1] for i in range(len(row)-1)):
            row.reverse()
            return


matrix = generate_random_matrix(4, 4, 1, 10)
print("Исходная матрица:")
for row in matrix:
    print(row)

find_and_reverse_ordered_row(matrix)

print("\nМатрица после изменения:")
for row in matrix:
    print(row)

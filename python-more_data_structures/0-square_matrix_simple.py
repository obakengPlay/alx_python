matrix = [[1,2,3], [4,5,6], [7,8,9]]

def square_matrix_simple(matrix=[]):
    test_matrix = []
    for row in matrix:
        new_row = [x ** 2 for x in row]
        test_matrix.append(new_row)
    return test_matrix

new_matrix = square_matrix_simple(matrix)

print(new_matrix)
print(matrix)

        
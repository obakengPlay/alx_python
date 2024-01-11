def print_matrix_integer(matrix=[]):
    
    for row in matrix:
        # Print each element in the row using str.format()
        for i in range(len(row)):
            if i == len(row) - 1:
                # If it's the last element in the row, print without a space
                print("{:d}".format(row[i]), end="")
            else:
                # Otherwise, print with a space after the element
                print("{:d} ".format(row[i]), end="")
        print()  # Move to the next line after printing a row
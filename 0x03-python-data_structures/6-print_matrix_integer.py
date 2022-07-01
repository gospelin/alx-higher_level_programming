#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for index, num in enumerate(matrix):
        # length = len(matrix[index]) - 1

        for j, digit in enumerate(matrix[index]):
            # if j = length:
            if digit == matrix[index][-1]:
                print("{:d}".format(digit), end='')
            else:
                print("{:d} ".format(digit), end='')
        print()

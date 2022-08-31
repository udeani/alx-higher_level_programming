#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    "function to print the square values of integers ina matrix"
    return ([list( map(lambda x: x * x, row)) for row in matrix])

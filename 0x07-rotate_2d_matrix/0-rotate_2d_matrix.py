#!/usr/bin/python3

"""
This script defines a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given 2D matrix 90 degrees clockwise.

    Args:
        matrix (list): The 2D matrix to be rotated. It should be a square
        matrix.
    Returns:
        None (The matrix is modified in-place).
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

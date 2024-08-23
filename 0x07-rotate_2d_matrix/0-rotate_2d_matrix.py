#!/usr/bin/python3
"""
Rotate 2D Matrix
current number, then top for left, then left for bottom, then botttom for right
then right for top.
"""

def rotate_2d_matrix(matrix):
    """rotate 2 dimensional matrix 90 degrees clockwise
    Args:
        matrix(list[[list]]): a matrix
    """

    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp  matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(n//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp

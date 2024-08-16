#!/usr/bin/python3
"""
Rotate 2D Matrix
current number, then top for left, then left for bottom, then botttom for right
then right for top
"""

def rotate_2d_matrix(matrix):
    """rotate 2 dimensional matrix 90 degrees clockwise
    Args:
        matrix(list[[list]]): a matrix
    """

    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n -i -1)
        for j in range(i, y):
            x = (n - i - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp

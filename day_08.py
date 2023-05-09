'''
    54. Spiral Matrix
    Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [1,2,3,6,9,8,7,4,5]
'''


def spiralOrder(matrix):
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)
    res = []

    while left < right and top < bottom:

        """ Print the first/top row from the remaining rows"""
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        """ Print the last/right column from the remaining columns"""
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        """Print the last/bottom row from the remaining rows"""
        if not (left < right and top < bottom):
            break
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        """Print the first/left column from the remaining columns"""
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res

n = int(input("Enter the number of subset: "))
matrix = []

for i in range(n):
    matrix.append([int(j) for j in input("Enter the elements: ").split()])
print(spiralOrder(matrix))
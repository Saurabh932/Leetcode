'''
    59. Spiral Matrix II
    Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

    Example 1:

        Input: n = 3
        Output: [[1,2,3],[8,9,4],[7,6,5]]
'''


def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]

    left, right = 0, n - 1
    top, bottom = 0, n - 1
    val = 1

    while left <= right:  # we can use top and bottom instead also. It will do the same work
        # Filling every value in top row
        for col in range(left, right + 1):
            matrix[top][col] = val
            val += 1
        top += 1

        # Filling every value in right column
        for row in range(top, bottom + 1):
            matrix[row][right] = val
            val += 1
        right -= 1

        # Filling every value in bottom row in reverse order
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = val
            val += 1
        bottom -= 1

        # Fillin every value in left column in reverse order
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = val
            val += 1
        left += 1

    return matrix

n = int(input("Enter the size: "))
print(generateMatrix(n))
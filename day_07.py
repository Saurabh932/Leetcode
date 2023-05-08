'''
    1572. Matrix Diagonal Sum
    Given a square matrix mat, return the sum of the matrix diagonals.

    Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal
    that are not part of the primary diagonal.

    Example 1:
            Input: mat = [[1,2,3],
                          [4,5,6],
                          [7,8,9]]
            Output: 25
            Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
            Notice that element mat[1][1] = 5 is counted only once.
'''


def diagonalSum(mat):
    res, n = 0, len(mat)

    for i in range(n):
        res += mat[i][i]  # Primary diagional
        res += mat[i][n - i - 1]  # Secondary diagional

    return res - (mat[n // 2][n // 2] if n % 2 else 0)


row = int(input("Enter the length of row: "))
col = int(input("Enter the length of col: "))
mat = []

for i in range(row):
    r = []
    for j in range(col):
        ele = int(input("Enter the elements: "))
        r.append(ele)
    mat.append(r)

print("The matrix = ")
for i in range(row):
    for j in range(col):
        print(mat[i][j], end=' ')
    print()

print("The sum of diagonal is: " ,diagonalSum(mat))

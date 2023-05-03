'''
    1822. Sign of the Product of an Array

    There is a function signFunc(x) that returns:

    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.
    You are given an integer array nums. Let product be the product of all values in the array nums.

    Return signFunc(product).

    Example 1:

    Input: nums = [-1,-2,-3,-4,3,2,1]
    Output: 1
    Explanation: The product of all values in the array is 144, and signFunc(144) = 1
'''


def signFunc(x):
    if x == 0:
        return 0
    elif x >= 1:
        return 1
    else:
        return -1
def arraySign(nums):
    if len(nums) == 0:
        return -1
    product = 1
    for i in nums:
        product *= signFunc(i)

    return product

nums = list(int(num) for num in input("Enter the elements: ").strip().split(","))
print(arraySign(nums))
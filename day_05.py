'''
    1498. Number of Subsequences That Satisfy the Given Sum Condition
    You are given an array of integers nums and an integer target.

    Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target.
    Since the answer may be too large, return it modulo 109 + 7.

    Example 1:

            Input: nums = [3,5,6,7], target = 9
            Output: 4
            Explanation: There are 4 subsequences that satisfy the condition.
            [3] -> Min value + max value <= target (3 + 3 <= 9)
            [3,5] -> (3 + 5 <= 9)
            [3,5,6] -> (3 + 6 <= 9)
            [3,6] -> (3 + 6 <= 9)
'''


def numSubseq(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0
    while left <= right:  # while the left pointer is less than or equal to the right pointer

        if nums[left] + nums[right] <= target:
            count += 2 ** (right - left)  # any subsequence that includes these two elements will be valid
            left += 1  # move the left pointer to the right

        else:
            right -= 1  # otherwise, move the right pointer to the left


    return count % (10 ** 9 + 7)  # return the count modulo 10^9 + 7

nums = list(int(num) for num in input("Enter the elements: ").strip().split(","))
target = int(input("Enter the target: "))
print(numSubseq(nums, target))
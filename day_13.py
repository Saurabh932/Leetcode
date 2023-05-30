'''
    1799. Maximize Score After N Operations

    You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

    In the ith operation (1-indexed), you will:

    Choose two elements, x and y.
    Receive a score of i * gcd(x, y).
    Remove x and y from nums.
    Return the maximum score you can receive after performing n operations.

    The function gcd(x, y) is the greatest common divisor of x and y.



    Example 1:

            Input: nums = [1,2]
            Output: 1
            Explanation: The optimal choice of operations is:
            (1 * gcd(1, 2)) = 1

    Example 2:

            Input: nums = [3,4,6,8]
            Output: 11
            Explanation: The optimal choice of operations is:
            (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
'''


def maxScore(nums):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def dfs(bitmask, nums, n, dp):
        if n == 0:
            return 0

        if bitmask in dp:
            return dp[bitmask]

        max_score = 0
        for i in range(len(nums)):
            if bitmask & (1 << i) == 0:
                for j in range(i + 1, len(nums)):
                    if bitmask & (1 << j) == 0:
                        score = gcd(nums[i], nums[j]) * n
                        bitmask |= (1 << i)
                        bitmask |= (1 << j)
                        curr_score = score + dfs(bitmask, nums, n - 1, dp)
                        max_score = max(max_score, curr_score)
                        bitmask &= ~(1 << i)
                        bitmask &= ~(1 << j)

        dp[bitmask] = max_score
        return max_score

    n = len(nums) // 2
    dp = {}
    return dfs(0, nums, n, dp)

'''
    1964. Find the Longest Valid Obstacle Course at Each Position
    You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, where obstacles[i] describes the height of the ith obstacle.

    For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course in obstacles such that:

    You choose any number of obstacles between 0 and i inclusive.
    You must include the ith obstacle in the course.
    You must put the chosen obstacles in the same order as they appear in obstacles.
    Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.
    Return an array ans of length n, where ans[i] is the length of the longest obstacle course for index i as described above.


    Example 1:

            Input: obstacles = [1,2,3,2]
            Output: [1,2,3,3]
            Explanation: The longest valid obstacle course at each position is:
            - i = 0: [1], [1] has length 1.
            - i = 1: [1,2], [1,2] has length 2.
            - i = 2: [1,2,3], [1,2,3] has length 3.
            - i = 3: [1,2,3,2], [1,2,2] has length 3.

'''

'''
    The problem asks to find the length of the longest increasing subsequence that can be formed using the given obstacle course. 
    The obstacle course consists of obstacles of different heights. You can only jump over obstacles with a height less than or equal to 
    your current height.

    Approach:
            For each obstacle, we compare it with the top of the stack, and if the current obstacle is greater than or equal to the top of the stack, we add it to the stack. Otherwise, we perform a binary search on the stack to find the index where the current obstacle can be inserted, and update the value at that index with the current obstacle.

            The length of the stack at each index gives us the length of the longest valid obstacle course that can be formed up to that index.
            
            Here's the step-by-step approach for this question:
            
            Initialize an empty stack.
            For each obstacle, compare it with the top of the stack:
            a. If the current obstacle is greater than or equal to the top of the stack, push it to the stack.
            b. Otherwise, perform a binary search on the stack to find the index where the current obstacle can be inserted.
                i. If the index is not found, it means the current obstacle is smaller than all the obstacles in the stack. 
                   In this case, add the obstacle to the end of the stack.
                ii. If the index is found, update the value at that index with the current obstacle.
            c. The length of the stack at each index gives us the length of the longest valid obstacle course 
               that can be formed up to that index. Return this list of lengths.

'''


def longestObstacleCourseAtEachPosition(obstacles):
    stack = []  # initialize the stack to keep track of obstacles
    longest_courses = []  # initialize the array to keep track of longest valid courses

    for obstacle in obstacles:  # iterate through the list of obstacles
        # if the stack is empty or the current obstacle is higher than the top of the stack, add the current obstacle to the stack
        if not stack or obstacle >= stack[-1]:
            stack.append(obstacle)
            longest_courses.append(
                len(stack))  # the length of the longest valid course ending at the current obstacle is equal to the length of the stack
        else:
            # if the current obstacle is lower than the top of the stack, pop obstacles off the stack until we find one that is lower than the current obstacle, or until the stack is empty
            # while popping obstacles off the stack, update the longest valid course array accordingly
            left, right = 0, len(stack) - 1
            while left <= right:
                mid = (left + right) // 2
                if stack[mid] <= obstacle:
                    left = mid + 1
                else:
                    right = mid - 1
            stack[left] = obstacle
            longest_courses.append(
                left + 1)  # the length of the longest valid course ending at the current obstacle is equal to the index of the lowest obstacle that is greater than or equal to the current obstacle in the stack, plus 1

    return longest_courses


obstacle = list(int(num) for num in input("Enter the elements: ").strip().split(","))
print(longestObstacleCourseAtEachPosition(obstacle))
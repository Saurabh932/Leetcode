'''
    1491. Average Salary Excluding the Minimum and Maximum Salary

    You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
    Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

    Example 1:

            Input: salary = [4000,3000,1000,2000]
            Output: 2500.00000
            Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
            Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

'''


def average(salary):
    salary = sorted(salary)
    count = 0
    max_salary = 0
    for i in range(1, len(salary) - 1):
        max_salary += salary[i]
        count += 1

    avg_salary = max_salary / count
    return avg_salary

salary = list(int(num) for num in input("Enter the salarys: ").strip().split(","))
print("The average salary: ",average())
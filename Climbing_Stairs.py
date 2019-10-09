# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climnStairs(n):
    store = {}

    def helper(n):
        # base case
        if n == 1 or n == 2:
            return n
        # check if stored in dictionary
        elif n in store:
            return store[n]
        else:
            # recursive function
            store[n] = helper(n-1) + helper(n-2)
            return store[n]
    return helper(n)

# 1 returns 1
# 2 returns 2

# For 3
#     1) goes through helper
#     2) store[n] = 2 + 1
#     3) 3 returns 3

# For 4
# 1) Goes through helper
# 2) First iteration
#     store[n] = 3 + 2
#     2a) Second iteration left helper when value is 3 (4-1)
#         store[n]= 2 + 1
#         value of left iteration = 3
#     2b) Second iteration right help when value is 2 (4-2)
# 3) Value = 3 + 2 = 5, 4 has 5 different options for staircase

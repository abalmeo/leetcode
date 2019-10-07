# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Time complexity : O(n^2)


def two_sum(num_list, target):
    for i in range(num_list):
        for j in range(num_list):
            value = num_list[i] + num_list[j]

            if target == value and i != j:
                return True
    return False

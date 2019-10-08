# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Time complexity : O(n^2)
# Brute force method


def two_sum_On2(num_list, target):
    length = len(num_list)
    for i in range(length):
        for j in range(length):
            value = num_list[i] + num_list[j]

            if target == value and i != j:
                print(num_list[i], num_list[j])
                return True
    return False


# Time complexity : O(n)
# Optimized
def two_sum_On(num_list, target):
    # store complement in dictionary or hashmap
    complementMap = dict()
    # loop through numbers
    for i in range(len(num_list)):
        num = num_list[i]
        # find complement of number for target
        complement = target - num
        print('num', num)
        print('complement', complement)
        # if number in complementMap, then complement exists that was looped through before
        if num in complementMap:
            return [complementMap[num], i]
        # if number not in complementMap, then add to comlpement map
        else:
            complementMap[complement] = i

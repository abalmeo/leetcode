# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        length = len(nums)
        # length - 2 because there are left and right pointers when looping through
        for i in range(length-2):
            # checking for duplicate 0s
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # left and right pointers
            l = i+1
            r = length-1
            # making sure not looking at the same inde
            while l < r:
               # checking total = 0
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l = l + 1
                elif total > 0:
                    r = r-1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # checking if indexes are not the same for l and r and if duplicates are used for left and right pointer
                    while l < r and nums[l] == nums[l+1]:
                        l = l+1
                    # checking if indexes are not the same for l and r and if duplicates are used for left and right pointer
                    while l < r and nums[r] == nums[r-1]:
                        r = r-1
                    l = l+1
                    r = r-1

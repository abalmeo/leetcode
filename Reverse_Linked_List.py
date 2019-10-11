# Reverse a singly linked list.

# Example:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev


# first iterations step wise
# 1) previous=none
# 1) temp=1
# 2) head=2
# 3) temp.next=none
# 4) prev=1
# Will continue and change links backwards until this reaches the end

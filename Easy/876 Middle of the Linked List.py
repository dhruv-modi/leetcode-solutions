# https://leetcode.com/problems/middle-of-the-linked-list/

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Note:

# The number of nodes in the given list will be between 1 and 100.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow_pointer = fast_pointer =  head
        while fast_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer.next if fast_pointer.next else slow_pointer
        
        

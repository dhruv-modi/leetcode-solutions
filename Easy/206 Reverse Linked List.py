# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        next_node =  head.next
        current_node = head
        
        while next_node:
            current_node.next = next_node.next
            next_node.next = head
            head = next_node
            next_node = current_node.next
        return head

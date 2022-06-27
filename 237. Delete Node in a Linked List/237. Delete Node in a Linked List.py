# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        prev_node = None
        while node.next:
            node.val = node.next.val
            prev_node = node
            node = node.next

        prev_node.next = None   
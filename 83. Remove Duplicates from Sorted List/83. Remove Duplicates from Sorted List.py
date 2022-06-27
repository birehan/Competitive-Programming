# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):

        while head and head.next and head.val == head.next.val:
            head = head.next

        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next if temp.next.next else None
            else:
                temp = temp.next

        return head

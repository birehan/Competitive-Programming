# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):

        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next

        values.sort(reverse=True)
        temp = head
        while temp and values:
            temp.val = values.pop()
            temp = temp.next

        return head
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next

        for i in range(0, len(values), 2):
            if i + 1 < len(values):
                values[i], values[i + 1] = values[i + 1], values[i]
        values.reverse()
        temp = head

        while temp:
            temp.val = values.pop()
            temp = temp.next

        return head

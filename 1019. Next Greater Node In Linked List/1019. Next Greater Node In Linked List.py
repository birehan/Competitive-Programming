# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        answer = [0] * len(values)
        stack = []

        for i in range(len(values)):

            while stack and values[i] > values[stack[-1]]:
                answer[stack.pop()] = values[i]

            stack.append(i)

        return answer









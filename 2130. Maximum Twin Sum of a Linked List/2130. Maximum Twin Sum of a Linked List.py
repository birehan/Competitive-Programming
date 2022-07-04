from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        summ = []
        for i in range(len(values) // 2):
            twin_sum = values[i] + values[len(values) - 1 - i]
            summ.append(twin_sum)
        return max(summ)

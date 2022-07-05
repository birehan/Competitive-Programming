# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next
        values.sort(reverse=True)
        temp = head
        while temp:
            temp.val = values.pop()
            temp = temp.next
        return head

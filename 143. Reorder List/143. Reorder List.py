# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next
        temp = head
        index = 0
        while temp:
            temp.val = values.pop(index)
            index = -1 if index == 0 else 0
            temp = temp.next

     
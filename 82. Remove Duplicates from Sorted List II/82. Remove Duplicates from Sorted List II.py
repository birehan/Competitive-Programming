# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        while head and head.next:
            if head.val == head.next.val:
                value = head.val
                while head and head.val == value:
                    head = head.next
            else:
                break

        if not head:
            return head

        temp = head.next
        prev = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                value = temp.val
                while temp and value == temp.val:
                    temp = temp.next
            else:
                prev.next = temp
                prev = prev.next
                temp = temp.next
        prev.next = temp

        return head


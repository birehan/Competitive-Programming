# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        head = l1
        prev = None
        while l1 and l2:
            val = l1.val + l2.val
            l1.val = (val + rem)%10
            rem= (val + rem)//10
            prev = l1
            l1 = l1.next
            l2 = l2.next
        
        left_over = l1 or l2
        while left_over:
            val =(left_over.val+rem)%10
            rem= (left_over.val+rem)//10

            left_over.val = val
            prev.next = left_over

            prev = prev.next
            left_over = left_over.next

        if rem:
            prev.next = ListNode(rem)

        return head
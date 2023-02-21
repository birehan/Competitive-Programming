# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head : return head

        length = 1
        temp = head
        while temp.next:
            length += 1
            temp = temp.next

        temp.next = head
        index = (length - (k%length))
        while index  > 0:
            temp = temp.next
            index -= 1
        
        front = temp.next
        temp.next = None

        return front
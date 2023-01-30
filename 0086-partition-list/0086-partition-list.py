# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        start = temp =  head

        while temp:
            if temp.val < x:
                hold = start
                value = temp.val 
                while hold != temp:
                    hold.val, value = value, hold.val
                    hold = hold.next

                hold.val = value
                start = start.next
            
            temp = temp.next
        
        return head
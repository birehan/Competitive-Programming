# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        
        count = count - n
        temp = head
        
        if count == 0:
            return head.next
        
        while count > 1:
            count -= 1
            temp = temp.next
            
    
        temp.next = temp.next.next
        
        return head
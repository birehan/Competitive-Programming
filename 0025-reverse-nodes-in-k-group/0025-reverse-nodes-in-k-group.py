# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def listLength(temp=head):
            length = 0
            while temp:
                temp = temp.next
                length += 1
            return length
        
        previous = last = None
        temp = head
        for i in range(listLength()//k):
            prev = prev_head = None
            for j in range(k):
                cur, temp = temp, temp.next
                cur.next = prev
                prev = cur
                if not prev_head and prev:
                    prev_head = prev
            
            if not previous:
                previous = prev
            else:
                last.next = prev
            last = prev_head
        
        if last:
            last.next = temp
            
        return previous
                
            
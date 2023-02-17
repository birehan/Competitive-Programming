# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        values = []
        temp = head
        while temp:
            if  left <= index <= right :
                values.append(temp.val)
            temp = temp.next
            index += 1

        values.reverse()
        index = 1
        temp = head
        p = 0
        while temp:
            if  left <= index <= right :
                temp.val = values[p]
                p += 1
            temp = temp.next
            index += 1
        
        return head


        


        
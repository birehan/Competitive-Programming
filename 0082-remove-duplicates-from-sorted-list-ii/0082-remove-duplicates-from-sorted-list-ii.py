# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=101, next=head)
        temp = dummy.next
        prev = dummy

        while temp and temp.next:
            if temp.val == temp.next.val:
                value = temp.val
                while temp and temp.val == value:
                    prev.next = temp.next
                    temp = temp.next
            else:
                prev = temp
                temp = temp.next
        
        return dummy.next
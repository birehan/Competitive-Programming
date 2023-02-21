# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        dummy = ListNode(val=5001, next=head)
        temp_head = dummy.next
        
        while temp_head:
            temp = temp_head
            min_val = temp
            while temp:
                if temp.val < min_val.val:
                    min_val = temp
                temp = temp.next
            temp_head.val, min_val.val = min_val.val, temp_head.val
            temp_head = temp_head.next


        return dummy.next
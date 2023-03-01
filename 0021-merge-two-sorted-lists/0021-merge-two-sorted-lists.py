# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMerged(self, list1, list2, merged):
        if not list1 and not list2:
            return

        if (list1 and not list2) or(list1 and list2 and (list1.val < list2.val)):
            merged.next = list1
            self.getMerged(list1.next, list2, merged.next)
        
        elif (list2 and not list1) or (list1 and list2 and  list2.val <= list1.val):
            merged.next = list2
            self.getMerged(list1, list2.next, merged.next)
        
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        merged = head
        self.getMerged(list1, list2, merged)
        return head.next


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nextListNodet
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        if not lists:
            return None
        
        for item in lists:
            while item:
                heappush(heap, item.val)
                item = item.next
        
        head = ListNode(0)
        temp = head
        while heap:
            temp.next = ListNode(heappop(heap))
            temp = temp.next

        return head.next


            

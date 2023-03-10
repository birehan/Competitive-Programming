# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def divide(self, head):
        temp = head
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow
    
    def conquer(self, root1, root2):
        head = ListNode()
        merged = head
        
        while root1 and root2:
            if root1.val < root2.val:
                merged.next = root1
                root1 = root1.next
            else:
                merged.next = root2
                root2 = root2.next
            merged = merged.next
        merged.next = root1 or root2
        
        return head.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or (not head.next):
            return head
        
        mid = self.divide(head)        
        root1 = self.sortList(head)
        root2 = self.sortList(mid)
        merged = self.conquer(root1, root2)

        return merged

        

        
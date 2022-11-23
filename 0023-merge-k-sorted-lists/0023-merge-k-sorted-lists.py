# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nextListNodet
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(list1, list2):
            if not list1 or not list2:
                return list1 or list2
            prev = head = None
            temp = list1
            while temp and list2:
                if list2.val < temp.val:
                    if not prev:
                        cur = list2
                        list2 = list2.next
                        cur.next = temp
                        prev, temp = cur, cur
                        temp = temp.next
                    else:
                        cur = temp
                        prev.next = list2
                        list2 = list2.next
                        prev = prev.next
                        temp = prev
                        temp.next = cur
                        temp = temp.next
                else:
                    prev = temp
                    temp = temp.next
                if prev and not head:
                    head = prev
            if list2:
                prev.next = list2

            return head
       
        if not lists:
            return None

        head = lists[0]
        for i in range(1, len(lists)):
            head = merge(head, lists[i])
            
        return head
      
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def get_len(node):
            count = 0
            while node:
                count += 1
                node = node.next

            return count
        
        self.len_1, self.len_2 = get_len(l1), get_len(l2)

        if self.len_2 > self.len_1:
            l1, l2 = l2, l1
            self.len_1, self.len_2 = self.len_2, self.len_1
        
        
        def summ(l1, l2):
            if not l1 and not l2:
                return 0
                
            if self.len_1 > self.len_2:
                self.len_1 -= 1
                val = summ(l1.next, l2) + l1.val

                l1.val = val % 10
                return val // 10
            
            else:
                val = summ(l1.next, l2.next) + l1.val + l2.val
                l1.val = val % 10
                return val // 10

        val = summ(l1, l2)
        if val:
            node = ListNode(val, l1)
            return node

        return l1 


                


        
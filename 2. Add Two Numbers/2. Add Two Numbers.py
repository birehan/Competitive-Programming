# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        result = None
        head = None
        rem = 0

        while l1 and l2:
            summ = l1.val + l2.val + rem
            value = summ % 10
            if not result:
                result = ListNode(value)
                head = result
            else:
                result.next = ListNode(value)
                result = result.next

            l1 = l1.next
            l2 = l2.next
            rem = summ // 10

        while l1:
            summ = l1.val + rem
            value = summ % 10
            rem = summ // 10
            if not result:
                result = ListNode(value)
                head = result
            else:
                result.next = ListNode(value)
                result = result.next
            l1 = l1.next

        while l2:
            summ = l2.val + rem
            value = summ % 10
            rem = summ // 10
            if not result:
                result = ListNode(value)
                head = result
            else:
                result.next = ListNode(value)
                result = result.next
            l2 = l2.next

        if rem != 0:
            result.next = ListNode(rem)

        return head

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        merged_list = []
        while list1 != None or list2 != None:
            if (list1 and list2):
                if (list1.val < list2.val):
                    merged_list.append(list1.val)
                    list1 = list1.next
                elif (list1.val > list2.val):
                    merged_list.append(list2.val)
                    list2 = list2.next
                else:
                    merged_list.append(list1.val)
                    merged_list.append(list2.val)
                    list1 = list1.next
                    list2 = list2.next
            elif (list1 and not list2):
                merged_list.append(list1.val)
                list1 = list1.next
            elif (list2 and not list1):
                merged_list.append(list2.val)
                list2 = list2.next

        def helper(merged_list):
            if len(merged_list) == 0:
                return None

            root = ListNode()
            root.val = merged_list[0]
            root.next = helper(merged_list[1:])

            return root

        return helper(merged_list)

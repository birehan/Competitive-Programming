# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        res = [0] * len(values)
        heap = [values[-1]]
        heapq.heapify(heap)
        
        for i in range(len(values)-2, -1, -1):
            while heap and heap[0] <= values[i]:
                 heapq.heappop(heap)

            if heap:
                res[i] = heap[0]
            heapq.heappush(heap, values[i])
        
        return res
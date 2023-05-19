class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heap.extend([element for row in matrix for element in row])
        heapify(heap)

        for _ in range(k-1):
            heappop(heap)

        return heappop(heap)
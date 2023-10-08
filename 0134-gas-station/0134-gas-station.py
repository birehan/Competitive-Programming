class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        heap = []
        n = len(gas)
        diff =  [gas[i] - cost[i] for i in range(n)]
        diff = [0] + diff + diff
        diff = list(accumulate(diff))

        left = 1
        for right in range(1, len(diff)):
            heappush(heap, (diff[right], right))

            if (right - left) == n:
                while heap and heap[0][1] < left:
                    heappop(heap)

                
                if heap[0][0] >= 0 or (-diff[left-1] > 0 and -diff[left-1] >=  abs(heap[0][0])):
                    return left-1
                
                left += 1
        
        return -1
      
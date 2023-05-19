class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = [(nums1[0]+nums2[0], 0, 0)]
        heapify(pairs)
        
        answer = []
        visited = {(0, 0)}
        while pairs and k:
            summ, a, b = heappop(pairs)
            k -= 1
            answer.append([nums1[a], nums2[b]])
            
            if a + 1 < len(nums1) and (a+1, b) not in visited:
                heappush(pairs, (nums1[a+1]+nums2[b], a+1, b))
                visited.add((a+1, b))

            if b + 1 < len(nums2) and (a, b+1) not in visited:
                heappush(pairs, (nums1[a]+nums2[b+1], a, b+1))
                visited.add((a, b+1))


        return answer

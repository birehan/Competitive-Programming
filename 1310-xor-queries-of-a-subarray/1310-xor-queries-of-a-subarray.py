class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        
        answer = []
        for left, right in queries:
            answer.append(arr[right] ^ (arr[left-1] if left > 0 else 0))
        
        return answer

        
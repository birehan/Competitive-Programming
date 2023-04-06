class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adjecents = {i for i in range(n)}
        for i, j in edges:
            if j in adjecents:
                adjecents.remove(j)

        return adjecents
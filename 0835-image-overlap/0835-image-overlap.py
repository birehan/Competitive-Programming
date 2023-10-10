class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        get_dirs = lambda i, j: [[i, j], [i, -j], [-i, j], [-i, -j], [j, i], [j, -i], [-j, i], [-j, -i]]
        
        n = len(img1)

        def get_value(i, j):
            count = 0
            for r in range(n):
                for c in range(n):
                    new_r, new_c = r + i, c + j
                    if 0 <= new_r < n and 0 <= new_c < n:
                        if img1[r][c] and img2[new_r][new_c]:
                            count += 1
            return count
            
        max_count = get_value(0, 0)

        for i in range(n):
            for j in range(i, n):
                for r, c in get_dirs(i, j):
                    cur_count = get_value(r, c)
                    max_count = max(max_count, cur_count)
        
        return max_count

        
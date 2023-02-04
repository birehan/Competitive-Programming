class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = defaultdict(str)
        row_count = 0
        forward = True
        
        for i in range(len(s)):
            if row_count + 1 < numRows and forward:
                rows[row_count] += s[i]
                row_count += 1
            else:
                rows[row_count] += s[i]
                row_count -= 1
                forward = False

                if row_count == 0:
                    forward = True
                            
        return "".join(rows.values())
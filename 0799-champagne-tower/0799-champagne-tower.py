class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]

        for i in range(query_row):
            new_row = []
            for j in range(len(row)):
                value = (row[j] - 1)/2 if row[j] >= 1 else 0
                if len(new_row) == 0:
                    new_row.append(value)                    
                else:
                    new_row[-1] += value
                    
                new_row.append(value)
            
            row = new_row
        
        return 1 if row[query_glass] >= 1 else row[query_glass] 






        
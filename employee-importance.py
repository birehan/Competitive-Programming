class Solution:
    def dfs(self,employee):
        if not employee.subordinates:
            return employee.importance

        cur_importance = employee.importance
        for subid in employee.subordinates:
            cur_importance  += self.dfs(self.dic[subid])
        
        return cur_importance

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.dic = dict([(emp.id, emp) for emp in employees])
        return self.dfs(self.dic[id])
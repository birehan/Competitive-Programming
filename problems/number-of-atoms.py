class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.index = 0
        
        def dfs():
            if self.index >= len(formula):
                return Counter()
            
            store = Counter()
            is_bracket = False
            while self.index < len(formula) :
                if formula[self.index].isupper():
                    element = formula[self.index]
                    self.index += 1
                    while self.index < len(formula) and formula[self.index].islower():
                        element += formula[self.index]
                        self.index += 1
                    
                    times = ""
                    while self.index < len(formula) and formula[self.index].isdigit():
                        times += formula[self.index]
                        self.index += 1
                    
                    times = int(times) if times else 1

                    if element in store:
                        store[element] += times
                    else:
                        store[element] = times
                    

                elif formula[self.index] == "(":
                    self.index += 1
                    cur = dfs()
                    times = ""
                    while self.index < len(formula) and formula[self.index].isdigit():
                        times += formula[self.index]
                        self.index += 1
                    
                    if times:
                        for key in cur:
                            cur[key] *= int(times)
                    
                    store = store + cur
                    
                elif formula[self.index] == ")":
                    self.index += 1
                    return store
            
            return store
        

        store = dfs()
        store = sorted(store.items())
        ans = []
        for elemnt, count in store:
            ans.append(elemnt)
            if count > 1:
                ans.append(str(count))
        
        return "".join(ans)




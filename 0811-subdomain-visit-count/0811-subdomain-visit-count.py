class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        dic = {}
        for item in cpdomains:
            count, site = item.split()
            index = 0
            dic[site] = int(count) + dic.get(site, 0)
            for index, value in enumerate(site):
                if value == ".":
                    cur = site[index+1:]
                    dic[cur] = int(count) + dic.get(cur, 0)
        
        res = []
        for key, value in dic.items():
            cur = str(value) + " " + key
            res.append(cur)
        
        return res
            
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for string in paths:
            paths = string.split()

            for i in range(1, len(paths)):
                cur =  paths[i].split("(")
                file_name, content = cur[0], cur[1][:-1]
                source = paths[0] + "/" + file_name.strip()
                dic[content].append(source)

        res = []
        for key, value in dic.items():
            if len(value) > 1:
                res.append(value)

        return res
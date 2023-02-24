class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        print(paths)
        for path in paths:
            if stack and path == "..":
                stack.pop()
                stack.pop()
            if path not in ["", ".", ".."]:
                stack.append("/")
                stack.append(path)
                
        return "".join(stack) if stack else "/"
class TreeNode:
    def __init__(self, parent=-1, isLocked=False, lockedBy=None, value=1):
        self.parent = parent
        self.isLocked = isLocked
        self.lockedBy = lockedBy
        self.value = value
        self.children = []

class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = self.buildGraph(parent)

    def buildGraph(self, parent):
        graph = defaultdict(TreeNode)
        for i in range(len(parent)):
            graph[i]= TreeNode(value=i)

        for i in range(len(parent)):
            cur = graph[i]
            cur.parent = parent[i]
            if parent[i] != -1:
                cur_parent = graph[parent[i]]
                cur_parent.children.append(cur)
            
        return graph
    
    def validateUpgrade(self, num):
        node = self.graph[num]

        if node.isLocked:
            return False
       
        hasLockedChild = False
        childrens = node.children.copy()
        while childrens:
            child = childrens.pop()
            if child.isLocked:
                hasLockedChild = True
                break
            
            childrens.extend(child.children.copy())
        

        if not hasLockedChild:
            return False
        
        hasLockedAncestor = False
        cur_parent = None
        while cur_parent != -1:
            cur_parent = node.parent 
            if self.graph[cur_parent].isLocked:
                hasLockedAncestor = True
                break
        
            node = self.graph[node.parent]
        
        if hasLockedAncestor:
            return False
        

        
        return True 

    def unlock_childrens(self, node):
        if not node.children:
            return
        
        for child in node.children:
            self.unlock(child.value, "upgrade")
            self.unlock_childrens(child)

    def lock(self, num: int, user: int) -> bool:
        node = self.graph[num]
        if node.isLocked:
            return False

        node.isLocked = True
        node.lockedBy = user


        return True

    def unlock(self, num: int, user: int) -> bool:     
        node = self.graph[num]
        if node.isLocked and (node.lockedBy == user or user == "upgrade"):
            node.isLocked = False
            node.lockedBy = None

            return True

        return False

    def upgrade(self, num: int, user: int) -> bool:
        if not self.validateUpgrade(num):
            return False
        
        self.lock(num, user)
        self.unlock_childrens(self.graph[num])
      
        return True

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.size = -1
        self.head = Node()


    def get(self, index: int) -> int:
        if index > self.size:
            return -1
        count = 0
        temp = self.head.next
        while count < index and temp:
            temp = temp.next
            count += 1

        return temp.val
        
    def addAtHead(self, val: int) -> None:
        temp = self.head.next
        new_node = Node(val=val, next=temp)
        self.head.next = new_node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        temp = self.head
        while temp.next:
            temp = temp.next

        new_node = Node(val=val)
        temp.next = new_node
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index-1 > self.size:
            return  
        prev = self.head
        cur = self.head.next
        while index > 0 and cur:
            cur = cur.next
            prev = prev.next
            index -= 1
        
        new_node = Node(val=val, next=cur)
        prev.next= new_node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size:
            return

        prev = self.head
        cur = self.head.next 
        while index > 0 and cur:
            index -= 1
            cur = cur.next
            prev = prev.next
            
        prev.next = cur.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
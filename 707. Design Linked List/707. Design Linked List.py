# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class MyLinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def get(self, index):
        size = 0
        temp = self.head

        while temp:
            if size == index:
                return temp.val
            temp = temp.next
            size += 1

        return -1

    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(val)

    def addAtIndex(self, index, val):
        if index == 0:
            node = ListNode(val)
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            size = 1

            while temp and temp.next:
                if size == index:
                    node = ListNode(val)
                    node.next = temp.next
                    temp.next = node

                last = temp
                temp = temp.next
                size += 1
            if size == index and temp:
                temp.next = ListNode(val)

    def deleteAtIndex(self, index):
        temp = self.head
        if index == 0 and temp:
            self.head = temp.next
        else:
            size = 1
            while temp and temp.next:
                if size == index:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                size += 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
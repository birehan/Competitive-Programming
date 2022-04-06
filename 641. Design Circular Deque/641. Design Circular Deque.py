class MyCircularDeque(object):

    def __init__(self, k):
        self.k = k
        self.deque = []
        """
        :type k: int
        """

    def insertFront(self, value):
        if len(self.deque) < self.k:
            self.deque.insert(0, value)
            return True
        else:
            return False
        """
        :type value: int
        :rtype: bool
        """

    def insertLast(self, value):
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        else:
            return False
        """
        :type value: int
        :rtype: bool
        """

    def deleteFront(self):
        if len(self.deque) != 0:
            self.deque.pop(0)
            return True
        else:
            return False
        """
        :rtype: bool
        """

    def deleteLast(self):
        if len(self.deque) != 0:
            self.deque.pop(-1)
            return True
        else:
            return False
        """
        :rtype: bool
        """

    def getFront(self):
        if len(self.deque) != 0:
            return self.deque[0]
        else:
            return -1
        """
        :rtype: int
        """

    def getRear(self):
        if len(self.deque) != 0:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self):

        return len(self.deque) == 0
        """
        :rtype: bool
        """

    def isFull(self):
        return len(self.deque) == self.k
        """
        :rtype: bool
        """

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
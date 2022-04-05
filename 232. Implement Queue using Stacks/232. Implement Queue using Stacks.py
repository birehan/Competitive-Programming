class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        """
        :type x: int
        :rtype: None
        """

    def pop(self):
        if self.empty():
            return
        return self.stack.pop(0)
        """
        :rtype: int
        """

    def peek(self):
        return self.stack[0]
        """
        :rtype: int
        """

    def empty(self):
        return len(self.stack) == 0
        """
        :rtype: bool
        """

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
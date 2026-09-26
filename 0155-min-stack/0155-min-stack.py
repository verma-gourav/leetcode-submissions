class MinStack(object):

    def __init__(self):
        self.stack = [] # pairs -> (val, curr_min)

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((value, value))
        else:
            curr_min = self.stack[-1][1]
            self.stack.append((value, min(value, curr_min)))

    def pop(self):
        """
        :rtype: None
        """
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]       

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
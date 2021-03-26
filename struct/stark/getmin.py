class NewStack(object):
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, value):
        self.stack.append(value)
        if self.stack_min == [] or value < self.getMin():
            self.stack_min.append(value)
        # return value

    def getMin(self):
        if self.stack_min:
            return self.stack_min[-1]
        return []

    def pop(self):
        value = self.stack.pop()
        if value == self.getMin():
            self.stack_min.pop()
        return value


s = NewStack()
print(s.push(1))
print(s.pop())
print(s.push(2))
print(s.push(3))
print(s.getMin())
print(s.push(1))
print(s.getMin())



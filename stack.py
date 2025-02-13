class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        return "Stack: " + str(self.stack)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)  # Stack: [10, 20, 30]
print(s.pop())  # 30
print(s.peek())  # 20
print(s.is_empty())  # False
print(s.size())  # 2

class PythonStack():
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) <= 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if len(self.stack):
            return self.stack[-1]

        return None

    def size(self):
        return len(self.stack)


sample_stack = PythonStack()
print(f'Is stack empty? {sample_stack.empty()}')

sample_stack.push(25)
print(f'Is stack empty? {sample_stack.empty()}')
print(f'Stack size: {sample_stack.size()}')

sample_stack.push(30)
sample_stack.push(35)
sample_stack.push(40)
sample_stack.push(45)
sample_stack.push(50)
sample_stack.push(55)
print(f'Stack size: {sample_stack.size()}')

print(sample_stack.peek())
print(sample_stack.pop())
# print(sample_stack.stack)
print(f'Stack size: {sample_stack.size()}')
print(sample_stack.peek())

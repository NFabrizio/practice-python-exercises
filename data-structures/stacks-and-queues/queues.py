class Node():
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class PythonQueue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Enqueue items
    # Create queue as a linked list so that enqueue and dequeue can be completed
    # in O(1) time complexity
    def enqueue(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1

            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    # Dequeue items
    def dequeue(self):
        curr_head = self.head

        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

        return curr_head

    # Get item at front of queue
    def front(self):
        return self.head

    # Get item at end of queue
    def back(self):
        return self.tail

    # Get size of queue
    def get_size(self):
        return self.size

    # Print queue
    def print_queue(self):
        curr_node = self.head

        while curr_node:
            print(f'value: {curr_node.value}, prev_node: {curr_node.prev}, next_node: {curr_node.next}')
            curr_node = curr_node.next


sample_queue = PythonQueue()

print(f'front() = {sample_queue.front()}, back = {sample_queue.back()}')

sample_queue.enqueue(50)
sample_queue.enqueue(100)
sample_queue.enqueue(150)
sample_queue.enqueue(200)
sample_queue.enqueue(250)

print(f'front() = {sample_queue.front()}, back = {sample_queue.back()}')
print(f'sample_queue size = {sample_queue.get_size()}')
sample_queue.print_queue()

print(sample_queue.dequeue().value)
print(sample_queue.dequeue().value)
print(f'sample_queue size = {sample_queue.get_size()}')
sample_queue.print_queue()

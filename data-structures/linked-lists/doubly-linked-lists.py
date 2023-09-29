class Node():
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class LinkedListDouble():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Add item at head
    def insert_head(self, value):
        new_node = Node(value)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            self.head = new_node
            self.tail = new_node
            self.length += 1

    # Add item at tail
    def insert_tail(self, value):
        new_node = Node(value)

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        else:
            self.tail = new_node
            self.head = new_node
            self.length += 1

    # Add item in middle
    def insert_mid(self, value, idx):
        new_node = Node(value)
        prev_node = None
        curr_node = self.head

        for i in range(idx):
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next = new_node
        new_node.prev = prev_node
        curr_node.prev = new_node
        new_node.next = curr_node
        self.length += 1

    # Delete item
    def delete_node(self, value):
        curr_node = self.head
        prev_node = None

        if curr_node.value == value:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        else:
            prev_node = curr_node
            curr_node = curr_node.next

        while curr_node:
            if curr_node.value == value:
                next_node = curr_node.next

                prev_node.next = curr_node.next

                if next_node:
                    next_node.prev = curr_node.prev
                self.length -= 1

                return

            prev_node = curr_node
            curr_node = curr_node.next

    # Find item
    def find_node_by_value(self, value):
        curr_node = self.head

        while curr_node:
            if curr_node.value == value:
                return True

            curr_node = curr_node.next

        return False

    # Count items in list
    def list_length(self):
        return self.length

    # Print list
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(f'value: {curr_node.value}, prev: {curr_node.prev}, next: {curr_node.next}')

            curr_node = curr_node.next

    # Print list
    def print_list_reversed(self):
        curr_node = self.tail
        while curr_node:
            print(f'value: {curr_node.value}, prev: {curr_node.prev}, next: {curr_node.next}')

            curr_node = curr_node.prev


# # Insert some items at head and print list
# sample_list = LinkedListDouble()
# sample_list.insert_head(25)
# sample_list.insert_head(50)
# sample_list.insert_head(100)
# sample_list.insert_head(200)
# sample_list.print_list()

# # Insert some items at tail and print list
# sample_list = LinkedListDouble()
# sample_list.insert_tail(25)
# sample_list.insert_tail(50)
# sample_list.insert_tail(100)
# sample_list.insert_tail(200)
# sample_list.print_list()

# Insert some items in middle and print list
sample_list = LinkedListDouble()
sample_list.insert_tail(25)
sample_list.insert_tail(50)
sample_list.insert_tail(100)
sample_list.insert_tail(200)
sample_list.insert_mid(30, 1)
sample_list.insert_mid(120, 4)
sample_list.print_list()
print(f'List length = {sample_list.list_length()}')
sample_list.print_list_reversed()
print(f'Does value exist? {sample_list.find_node_by_value(10)}')
sample_list.delete_node(200)
sample_list.print_list()
print(f'List length = {sample_list.list_length()}')

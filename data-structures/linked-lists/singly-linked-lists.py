class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedListSingle():
    def __init__ (self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head

        self.head = new_node
        self.tail = new_node
        self.length += 1

    def insert_tail(self, value):
        new_node = Node(value)

        # # Naive approach
        # curr_node = self.head
        #
        # if curr_node is None:
        #     self.head = new_node
        #
        #     return
        #
        # while curr_node.next is not None:
        #     curr_node = curr_node.next
        #
        # curr_node.next = new_node
        # self.length += 1

        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.insert_head(value)

    def insert_mid(self, idx, value):
        new_node = Node(value)
        idx_count = 0
        curr_node = self.head
        prev_node = None

        # If idx is 0, just insert node at head
        if idx == 0:
            self.insert_head(value)
            return

        # If idx is greater than or equal to list length, insert at tail
        # This assumes that when a user tries to insert at an index that is out
        # of range we want to just append the value rather than return an error
        if idx >= self.length:
            self.insert_tail()
            return

        # Otherwise, find the correct index in the list and insert the node
        while curr_node and idx_count < idx:
            prev_node = curr_node
            curr_node = curr_node.next
            idx_count += 1

        # Make new_node.next curr_node
        new_node.next = curr_node

        # Make new_node the next of prev_node
        prev_node.next = new_node

        self.length += 1

    def find_node_by_value(self, target):
        curr_node = self.head

        while curr_node:
            if curr_node.value == target:
                return True

            curr_node = curr_node.next

        return False

    # def find_node_by_index(self, idx):
    def __getitem__(self, idx):
        if idx >= self.length or idx < 0:
            return Node(None)

        curr_node = self.head

        for i in range(idx):
            curr_node = curr_node.next

        return curr_node

    # def update_node(self, value, idx):
    def __setitem__(self, value, idx):
        if idx >= self.length or idx < 0:
            return Node(None)

        curr_node = self.head

        for i in range(idx):
            curr_node = curr_node.next

        curr_node.value = value

        return curr_node

    def delete_node(self, idx):
        idx_count = 0
        curr_node = self.head
        prev_node = None

        # If list is empty, stop and return
        if self.length == 0:
            return

        # If idx is 0, remove head
        if idx == 0:
            self.head = self.head.next
            self.length -= 1
            return

        # Assumes that if idx is greater than list length + 1, we will just
        # remove the last list item rather than return an error
        while curr_node.next and idx_count < idx:
            prev_node = curr_node
            curr_node = curr_node.next
            idx_count += 1

        prev_node.next = curr_node.next
        self.length -= 1

    def list_len(self):
        # # Naive approach
        # node_count = 0
        # curr_node = self.head
        #
        # while curr_node is not None:
        #     print(f'value: {curr_node.value}, next: {curr_node.next}')
        #
        #     curr_node = curr_node.next
        #
        #     node_count += 1
        #
        # return node_count

        return self.length

    def list_print(self):
        curr_node = self.head

        while curr_node is not None:
            print(f'value: {curr_node.value}, next: {curr_node.next}')

            curr_node = curr_node.next

sample_list = LinkedListSingle()

# Insert some items into the list and print out the result

# # sample_list.insert_head(15)
# # sample_list.insert_head(10)
# # sample_list.insert_head(5)
# # sample_list.list_print()
# sample_list.insert_tail(5)
# sample_list.insert_tail(10)
# sample_list.insert_tail(15)
# # sample_list.list_print()
#
# sample_list.insert_mid(1, 7)
# # sample_list.insert_mid(4, 20)
# sample_list.list_print()
#
# sample_list.delete_node(4)
# sample_list.list_print()
#
# print(f'List length = {sample_list.list_len()}')

# Search for a specific item in the list and return a boolean based on whether or not it exists

# sample_list.insert_tail(5)
# sample_list.insert_tail(7)
# sample_list.insert_tail(12)
# sample_list.insert_tail(9)
# sample_list.insert_tail(13)
# sample_list.insert_tail(105)
#
# print(sample_list.find_node_by_value(105))

# Access specfic item using index value

# sample_list.insert_tail(5)
# sample_list.insert_tail(7)
# sample_list.insert_tail(12)
# sample_list.insert_tail(9)
# sample_list.insert_tail(13)
# sample_list.insert_tail(105)
#
# print(sample_list[8].value)


# Set new value of node using index

sample_list.insert_tail(5)
sample_list.insert_tail(7)
sample_list.insert_tail(12)
sample_list.insert_tail(9)
sample_list.insert_tail(13)
sample_list.insert_tail(105)
sample_list.list_print()

# sample_list.update_node(3, 8)
sample_list[3].value = 8
sample_list.list_print()

class Node():
    def __init__(self, value, left=None, right=None):
    # def __init__(self, value, left=[], right=[]):
        # print(left)
        # print(right)
        self.value = value
        if left:
            self.left = left
        else:
            self.left = None

        if right:
            self.right = right
        else:
            self.right = None

class BinarySearchTree():
    # Create a Balanced Binary Search Tree (BST) using an array of elements
    # where array elements are sorted in ascending order
    # Naive approach
    def build_balanced_bst(self, node_vals=None):
        if not node_vals:
            return None

        if len(node_vals) == 1:
            return Node(node_vals[0])

        root_idx = len(node_vals) // 2

        root = Node(node_vals[root_idx])

        root.left = self.build_balanced_bst(node_vals[:root_idx])
        root.right = self.build_balanced_bst(node_vals[root_idx + 1:])

        return root

    # Create a Balanced Binary Search Tree (BST) using an array of elements
    # where array elements are sorted in ascending order
    # Better approach
    def build_balanced_bst2(self, node_vals=None, left=0, right=None):
        if not node_vals or left < 0 or right < 0 or left > right:
            return None

        if len(node_vals) == 1:
            return Node(node_vals[0])

        if right == left:
            return Node(node_vals[left])

        if not right:
            right = len(node_vals) - 1

        root_idx = (right - left) // 2 + left

        root = Node(node_vals[root_idx])

        root.left = self.build_balanced_bst2(node_vals, left, root_idx - 1)
        root.right = self.build_balanced_bst2(node_vals, root_idx + 1, right)

        return root

    def node_search(self, root=None, target=None):
        if not root or not target:
            return Node(None)

        result = None

        if root.value == target:
            result = root
            return result

        next_node = root.left if root.value > target else root.right
        result = self.node_search(next_node, target)

        return result

    def node_insert(self, root=None, insertion=None):
        if not insertion:
            return root

        if not root:
            return Node(insertion)

        if root.value > insertion:
            root.left = self.node_insert(root.left, insertion)
        elif root.value < insertion:
            root.right = self.node_insert(root.right, insertion)

        return root


    def node_delete(self, root=None, target=None):
        if not root or not target:
            return Node(None)

        # target is on left side of BST
        if root.value > target:
            root.left = self.node_delete(root.left, target)
        # target is on right side of BST
        elif root.value < target:
            root.right = self.node_delete(root.right, target)
        # target is current node, so return the appropriate node instead, which
        # will effectively delete the current node through exclusion from the BST
        else:
            # If this node has only one child, stop and return that child. If no
            # children exist, stop and return None
            if not root.right or not root.left:
                return root.right if root.right else root.left

            # If both children exist, find the node with the largest value on
            # the left side of the remaining tree and replace the current node
            # with that node value
            curr_node = root.left
            max_value = curr_node.value

            while curr_node:
                max_value = curr_node.value
                curr_node = curr_node.right

            root.value = max_value

            # Replace current node left with updated BST where node with max
            # value is deleted
            root.left = self.node_delete(root.left, max_value)

        return root

    # Preorder = root-left-right
    def print_preorder(self, node):
        if not node:
            return None

        print(node.value)
        left = self.print_preorder(node.left)
        right = self.print_preorder(node.right)

        return

    def list_preorder(self, node, preorder_list=None):
        if not preorder_list:
            preorder_list = []

        if not node:
            return None

        preorder_list.append(node.value)
        left = self.list_preorder(node.left, preorder_list)
        right = self.list_preorder(node.right, preorder_list)

        return preorder_list

    # postorder = left-right-root
    def list_postorder(self, node, postorder_list=None):
        if not postorder_list:
            postorder_list = []

        if not node:
            return None

        left = self.list_postorder(node.left, postorder_list)
        if left:
            postorder_list = left

        right = self.list_postorder(node.right, postorder_list)
        if right:
            postorder_list = right

        postorder_list.append(node.value)

        return postorder_list

    def print_tree(self, node):
        if node and (node.left or node.right):
            print(f'node value: {node.value}')

            if node.left:
                print(f'node {node.value} left: {node.left.value}')
                self.print_tree(node.left)
            if node.right:
                print(f'node {node.value} right: {node.right.value}')
                self.print_tree(node.right)

        return



# node = Node(5, None, 5)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data2 = [1, 2, 3, 4, 5]
sample_tree = BinarySearchTree()
# root = sample_tree.build_balanced_bst(data)
root2 = sample_tree.build_balanced_bst(data2)
root22 = sample_tree.build_balanced_bst2(data2, 0, len(data2) - 1)

# sample_tree.print_tree(root)
# print()
sample_tree.print_tree(root2)
print()
sample_tree.print_tree(root22)
print()
# sample_tree.print_preorder(root2)
# print()
# sample_tree.print_preorder(root22)
# print()
print(f'root2 preorder: {sample_tree.list_preorder(root2)}')
print()
print(f'root22 preorder: {sample_tree.list_preorder(root22)}')
print()
print(f'root2 postorder: {sample_tree.list_postorder(root2)}')
print()
print(f'root22 postorder: {sample_tree.list_postorder(root22)}')
print()

matched = sample_tree.node_search(root2, 4)
print(f'matched val for target 4 = {matched.value}')
matched = sample_tree.node_search(root2, 1)
print(f'matched val for target 1 = {matched.value}')
matched = sample_tree.node_search(root2, 18)
print(f'matched val for target 18 = {matched.value}')

bigger_tree = sample_tree.node_insert(root2, 9)
bigger_tree = sample_tree.node_insert(root2, 7)
bigger_tree = sample_tree.node_insert(root2, -1)
print(f'Preorder after insertions: {sample_tree.list_preorder(bigger_tree)}')

new_tree_root = sample_tree.node_delete(root2, 1)
print(f'Preorder after deleting node with value of 1: {sample_tree.list_preorder(new_tree_root)}')

# new_tree_root = sample_tree.node_delete(root2, 3)
# print(f'Preorder after deleting node with value of 3: {sample_tree.list_preorder(new_tree_root)}')

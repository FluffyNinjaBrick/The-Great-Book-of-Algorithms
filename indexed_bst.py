
# an implementation of a BST whose nodes store the size of their subtrees, with methods for adding values,
# finding the ith largest value and finding the index (which largest is it) of a given value


class Node:
    def __init__(self, value):
        self.value = value
        self.left_count = 0
        self.right_count = 0
        self.right_child = None
        self.left_child = None

    def add(self, val):
        if self.value < val:
            self.right_count += 1
            if self.right_child is not None:
                self.right_child.add(val)
            else:
                self.right_child = Node(val)
        elif self.value > val:
            self.left_count += 1
            if self.left_child is not None:
                self.left_child.add(val)
            else:
                self.left_child = Node(val)

    def find_ith_largest(self, i):
        curr_node = self
        while True:
            if curr_node.right_count == i-1:
                return curr_node.value
            elif curr_node.right_count > i-1 and curr_node.right_child is not None:
                curr_node = curr_node.right_child
            elif curr_node.right_count < i-1 and curr_node.left_child is not None:
                i -= (curr_node.right_count + 1)
                curr_node = curr_node.left_child
            else:
                return "No such index exists"

    def find_index_of(self, val):
        curr_node = self
        index = curr_node.right_count + 1
        while True:
            if curr_node.value == val:
                return index
            elif curr_node.value < val and curr_node.right_child is not None:
                curr_node = curr_node.right_child
                index -= (curr_node.right_count + 1)
            elif curr_node.value > val and curr_node.left_child is not None:
                curr_node = curr_node.left_child
                index += 1 + curr_node.right_count
            else:
                return "No such value exists"


if __name__ == "__main__":
    tree = Node(2)
    tree.add(1)
    tree.add(4)
    tree.add(3)
    tree.add(5)
    tree.add(0)

    print(tree.find_ith_largest(1))
    print(tree.find_index_of(2))

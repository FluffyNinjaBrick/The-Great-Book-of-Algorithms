from typing import List

# an implementation of a span tree structure to solve the subarray sum problem


class SpanNode:
    def __init__(self, value, start, end):
        self.value = value  # this will hold the value if a leaf, or the sum of subarray values if a tree node
        self.start = start
        self.end = end
        self.parent: SpanNode = None
        self.left: SpanNode = None
        self.right: SpanNode = None


def numArrayToNodeArray(num_array: List):
    num_array.sort()
    node_array = []
    for i in range(len(num_array)):
        node_array.append(SpanNode(num_array[i], i, i))
    return node_array


def buildSpanTree(node_array: List[SpanNode]):

    # if the array contains one node, we know that it's the root and return it
    if len(node_array) == 1:
        return node_array.pop(0)

    higher_level_array = []

    # we pair lower level nodes into higher level ones, removing them from the array as we go
    while len(node_array) >= 2:
        left = node_array.pop(0)
        right = node_array.pop(0)
        higher_level_node = SpanNode(left.value + right.value, left.start, right.end)

        # assign the relations between the nodes
        left.parent = higher_level_node
        higher_level_node.left = left
        right.parent = higher_level_node
        higher_level_node.right = right

        higher_level_array.append(higher_level_node)

    # if there is one node left add it to the higher level list to be paired later
    if len(node_array):
        higher_level_array.append(node_array.pop(0))

    return buildSpanTree(higher_level_array)


def sumBetween(tree: SpanNode, start, end):
    if start > end:
        return 0

    if tree.start == start and tree.end == end:
        return tree.value

    left_end = min(tree.left.end, end)
    right_start = max(tree.right.start, start)
    return sumBetween(tree.left, start, left_end) + sumBetween(tree.right, right_start, end)


if __name__ == "__main__":
    nums = [i for i in range(10)]
    root = buildSpanTree(numArrayToNodeArray(nums))
    print(sumBetween(root, 3, 6))

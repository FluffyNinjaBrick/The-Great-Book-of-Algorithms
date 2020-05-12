
# can't help but feel that this is slightly overcomplicated

from collections import deque


class MaxHeap:
    def __init__(self):
        super().__init__()
        self.heap = deque()

    def push(self, elem):
        self.heap.append(elem)
        self.__float_up(len(self.heap) - 1)

    def pop(self):
        # case 1 - heap empty
        if not self.heap:
            return None
        # case 2 - heap contains 1 element
        if len(self.heap) == 1:
            return self.heap.popleft()
        # case 3 - heap contains multiple elements
        top = self.peek()
        self.heap[0] = self.heap.pop()
        self.__bubble_down(0)
        return top

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def __float_up(self, idx):
        if idx == 0:
            return
        parent = idx/2
        if self.heap[parent] < self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            self.__float_up(parent)
        return

    def __bubble_down(self, idx):
        left_child = 0
        right_child = 0

        if idx*2 >= len(self.heap):
            return
        else:
            left_child = idx*2

        if idx*2 + 1 >= len(self.heap):
            pass
        else:
            right_child = idx*2

        # case 1 - no children exist
        if left_child == 0 and right_child == 0:
            return

        # case 2 - both children exist
        if left_child > 0 and right_child > 0:
            if self.heap[left_child] > self.heap[right_child]:
                larger_child = left_child
            else:
                larger_child = right_child
            if self.heap[idx] < self.heap[larger_child]:
                self.heap[idx], self.heap[larger_child] = self.heap[larger_child], self.heap[idx]
                self.__bubble_down(larger_child)
            return

        # case 3 - only left child exists
        if self.heap[left_child] > self.heap[idx]:
            self.heap[idx], self.heap[left_child] = self.heap[left_child], self.heap[idx]
        return

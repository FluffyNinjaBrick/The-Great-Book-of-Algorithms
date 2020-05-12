from collections import deque

euler_stack = deque()

# If we know the graph has an Euler cycle, and all we need to do is find it, the implementation becomes
# much easier, boiling down to a simple DFS


def find_euler_cycle(graph, start_node):
    for i in range(len(graph)):
        if graph[start_node][i]:
            graph[start_node][i] = 0
            graph[i][start_node] = 0
            find_euler_cycle(graph, i)
    euler_stack.append(start_node)


if __name__ == "__main__":
    # the example from the lecture
    test_graph = [
        [0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 1, 1, 0]
    ]
    find_euler_cycle(test_graph, 0)
    print(euler_stack)




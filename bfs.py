
# Recursive BFS

visited = []
result = []


def bfs(graph, start_node, layer):
    visited.append(start_node)
    # check all neighbors of this node
    for i in range(len(graph)):
        if graph[start_node][i] == 1 and i not in visited:
            result.append((start_node, layer))
    # activate bfs for the nodes that were first discovered in this layer, if any
    for i in range(len(graph)):
        if graph[start_node][i] == 1 and i not in visited:
            bfs(graph, i, layer+1)


def bfs_wrapper(graph, start_node):
    result.append((None, start_node))
    bfs(graph, start_node, 1)


if __name__ == "__main__":
    test_graph = [[0, 1, 1, 0],
                  [0, 0, 0, 1],
                  [0, 1, 0, 1],
                  [0, 0, 0, 0]]
    bfs_wrapper(test_graph, 0)
    print(result)




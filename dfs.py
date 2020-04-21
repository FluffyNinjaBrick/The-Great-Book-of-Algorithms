
# Basic recursive DFS.


visited = []
result = []


def dfs(graph, curr_node, prev_node):
    visited.append(curr_node)
    result.append(prev_node)
    for neighbor in graph[curr_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, curr_node)


if __name__ == "__main__":
    test_graph = [[1, 2],
                  [0, 2, 3],
                  [3, 1, 0],
                  []]
    dfs(test_graph, 0, None)
    print(result)

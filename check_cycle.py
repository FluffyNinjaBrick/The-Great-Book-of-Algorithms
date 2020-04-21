
# Check if a graph contains a cycle. Untested, but it's simple enough, so it probably works.
# Graph is represented as neighbor lists


def dfs(graph, curr_node, prev_node):
    visited[curr_node] = True
    found = False
    for neighbor in graph[curr_node]:
        if neighbor == prev_node:
            continue
        if visited[neighbor]:
            return True
        else:
            if dfs(graph, neighbor, curr_node):
                found = True
    return found


if __name__ == "__main__":
    test_graph = [
        # put something in here
    ]
    n = len(test_graph)
    visited = [False for i in range(n)]
    for i in range(n):
        if not visited[i]:
            has_cycle = dfs(test_graph, 0, None)
            if has_cycle:
                print("Has cycle")
                break
    print("Doesn't have cycle")

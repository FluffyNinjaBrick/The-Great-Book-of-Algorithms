
# an algorithm for finding and recording the shortest paths to all nodes using BFS


from collections import deque

N = 5

visited = [False for i in range(N)]
parents = [None for i in range(N)]


def bfs(graph, source):
    q = deque()
    q.append(source)
    visited[source] = True
    parents[source] = source

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parents[neighbor] = node
                q.append(neighbor)


def print_path(node):
    if parents[node] != node:
        print_path(parents[node])
    print(node)


if __name__ == "__main__":
    test_graph = [
        [1, 3],
        [3, 4],
        [0, 1],
        [2],
        [0, 1, 2, 3]
    ]
    bfs(test_graph, 0)
    print_path(2)

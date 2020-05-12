

# simple implementation of the Floyd-Warshall shortest path algorithm

def findFW(paths):
    for k in range(len(paths)):
        for i in range(len(paths)):
            for j in range(len(paths)):
                paths[i][j] = min(paths[i][j], paths[i][k] + paths[k][j])
    return paths


if __name__ == "__main__":
    graph = [
        [0, 2, 7, float("inf"), float("inf"), float("inf")],
        [2, 0, float("inf"), 3, float("inf"), float("inf")],
        [7, float("inf"), 0, 3, 8, float("inf")],
        [float("inf"), 3, 3, 0, 1, 4],
        [float("inf"), float("inf"), 8, 1, 0, float("inf")],
        [float("inf"), float("inf"), float("inf"), 4, float("inf"), 0]
    ]

    print(findFW(graph))

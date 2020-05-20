
# An implementation of Kruskal's algorithm using find-union

# The return value is the set of edges that make up the minimum spanning tree


class Edge:
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end


class Node:
    def __init__(self, num):
        self.num = num
        self.parent = self
        self.rank = 0


def find_set(x):  # the root's parent is itself
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(edges):  # NOTE - this needs the edges to be sorted
    result = []
    for edge in edges:
        if find_set(edge.start) != find_set(edge.end):
            result.append(edge)
            union(edge.start, edge.end)
    return result


if __name__ == "__main__":
    A = Node(1)
    B = Node(2)
    C = Node(3)
    D = Node(4)
    E = Node(5)
    F = Node(6)
    G = Node(7)
    test_graph = [Edge(1, A, G), Edge(1, C, D), Edge(2, A, B), Edge(2, C, G), Edge(3, B, C), Edge(5, E, G),
                  Edge(6, F, A), Edge(7, D, E), Edge(8, E, F)]
    result = kruskal(test_graph)
    for edge in result:
        print("weight:", edge.weight, ", between nodes", edge.start.num, "and", edge.end.num)

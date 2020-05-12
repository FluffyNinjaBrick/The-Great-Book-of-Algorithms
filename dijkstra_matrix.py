
# the graph is shown as an array, where -1 means no edge,
# and a positive integer means a vertex with a given weight


class Vertex:
    def __init__(self):
        self.distance = float("inf")
        self.parent = None
        self.done = False


def relax(graph, i, j, nodes):
    if nodes[j].distance > nodes[i].distance + graph[i][j]:
        nodes[j].distance = nodes[i].distance + graph[i][j]
        nodes[j].parent = i


def dijkstra(graph, start_node):
    node_count = len(graph)

    nodes = [Vertex() for i in range(node_count)]

    nodes[start_node].distance = 0
    nodes[start_node].parent = start_node

    for i in range(node_count):
        minimum = float("inf")
        min_idx = 0

        for x in range(node_count):
            if nodes[x].distance < minimum and not nodes[x].done:
                minimum = nodes[x].distance
                min_idx = x

        for j in range(node_count):
            if graph[min_idx][j] != -1:
                relax(graph, min_idx, j, nodes)
        nodes[min_idx].done = True

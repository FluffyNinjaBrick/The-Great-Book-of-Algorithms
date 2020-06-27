
# an algorithm that finds the strongly connected components in a directed graph
# this algorithm represents graphs as matrices: graph[from][to], bool or int

# the algorithm goes as follows: fire up DFS while saving the times of processing, then invert
# all the edges and fire up DFS again, each time for the unvisited node that was processed last.

# This way, we will be starting with the SCC which is topologically the last, as it has no edges leading
# outside of itself. Therefore, the algorithm is correct.

# DISCLAIMER: this algorithm is a pain to implement. Either you use neighbor lists, which makes implementing
# the edge reversal tough, or - like here - you use a matrix, in which case the reversal is trivial, but
# the final step of writing out the SCCs becomes a bit complicated, because you can't really delete a node from
# a matrix-represented graph


# set of globals
size = 6
time = 0
visited = [False for _ in range(size)]
processed_at = [0 for _ in range(size)]


# this is actually the DFS subroutine, but we'll be calling it differently in the algorithm so no wrapper is needed
def dfs(graph, node):
    global time
    visited[node] = True
    for i in range(size):
        if not visited[i] and graph[node][i]:
            dfs(graph, i)
    time += 1
    processed_at[node] = time


# needed for the algorithm
def reverse_edges(graph):
    for i in range(size):
        for j in range(i, size):
            graph[i][j], graph[j][i] = graph[j][i], graph[i][j]


def max_in_list(li):
    max_num = 0
    max_idx = 0
    for i in range(len(li)):
        n = li[i]
        if n > max_num:
            max_num = n
            max_idx = i
    if max_num:
        return max_idx
    return -1


# the algorithm itself
if __name__ == "__main__":

    # the test graph shall be two triangular cycles connected one-way
    test_graph = [[False for _ in range(size)] for _ in range(size)]
    test_graph[0][1] = True
    test_graph[1][2] = True
    test_graph[2][0] = True
    test_graph[2][3] = True
    test_graph[3][4] = True
    test_graph[4][5] = True
    test_graph[5][3] = True

    # step 1
    for num in range(size):  # in this test case this loop is technically unnecessary, but usually it's needed
        if not visited[num]:
            dfs(test_graph, num)

    # step 2
    reverse_edges(test_graph)

    # step 3
    # we find the latest-visited node, find the SCC that contains it, and zero all the visit times for
    # that SCC so that we don't check it again
    scc_idx = 1

    # this exists because we can't actually remove nodes from the graph, so we just have to say
    # that they are "not there"
    already_another_scc = []

    while True:
        scc_nodes = []
        visited = [False for _ in range(size)]
        latest_node = max_in_list(processed_at)
        if latest_node == -1:
            break
        dfs(test_graph, latest_node)
        for i in range(size):
            if visited[i] and i not in already_another_scc:
                scc_nodes.append(i)
                already_another_scc.append(i)
        for done in already_another_scc:
            processed_at[done] = 0
        print(f"Strongly Connected Component {scc_idx}:\n")
        print(scc_nodes)
        scc_idx += 1

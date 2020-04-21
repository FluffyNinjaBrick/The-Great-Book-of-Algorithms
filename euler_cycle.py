from collections import deque

euler_stack = deque()


# this function discovers a subset of the euler cycle, which is in itself a cycle
# it returns one if a cycle is found, and 0 if no cycle - and therefore no euler cycle - exists
def find_cycle_dfs(graph, curr_node, cycle_start):
    # if the cycle can be completed we do so
    if graph[curr_node][cycle_start]:
        euler_stack.append(cycle_start)
        graph[curr_node][cycle_start] = 0
        graph[cycle_start][curr_node] = 0
        return 1
    # if the cycle cannot be completed...
    for i in range(len(graph)):
        # we enter any of the existing vertices from the current node and search from there
        if graph[curr_node][i]:
            euler_stack.append(i)
            graph[curr_node][i] = 0
            graph[i][curr_node] = 0
            return find_cycle_dfs(graph, i, cycle_start)
        # if the function reaches this part, we have found a dead end and the graph does not contain an Euler cycle
    print("Graph does not contain euler cycle")
    return 0


def find_euler_cycle(graph, start_node):
    # instantiate return stack and add start node to Euler stack
    euler_stack.append(start_node)
    return_list = deque()
    # find an initial cycle
    find_cycle_dfs(graph, start_node, start_node)
    # move through the found cycle, find additional cycles from nodes which still have outgoing vertices
    while euler_stack:
        # grab top of stack
        node = euler_stack.pop()
        euler_stack.append(node)
        # check if it still has vertices
        for i in range(len(graph)):
            # if a vertex is found, activate the cycle finder
            if graph[node][i]:
                found_cycle = find_cycle_dfs(graph, node, node)
                # if the cycle finder fails to find a cycle, the graph does not contain an Euler cycle and we can finish
                if not found_cycle:
                    return []
        # once that is done, we know that the node at the top of the Euler stack has no vertices and can be moved
        # to the result
        return_list.append(euler_stack.pop())
    # the return list contains the order in which to visit the nodes to cover an Euler cycle
    return return_list


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
    result = find_euler_cycle(test_graph, 0)
    print(result)




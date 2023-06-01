from collections import deque


def breadth_first_search(graph, start_node):
    visited = set([start_node])

    queue = deque([start_node])

    while queue:

        curr_node = queue.popleft()
        print(curr_node)

        # enqueue the unvisited neighbours
        for neighbour in graph[curr_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    # graph = {
    #     'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': ['G'],
    #     'E': [],
    #     'F': [],
    #     'G': []
    # }

    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}

    start_node = 0

    breadth_first_search(graph, start_node)

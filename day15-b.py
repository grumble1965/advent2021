import sys
import numpy as np
import heapq
import itertools


# priority queue implemented via heapq
pq = []
entry_finder = {}
REMOVED = '<removed-task>'
counter = itertools.count()


def add_task(task, priority=0):
    """Add a new task or update the priority of an existing task"""
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)


def remove_task(task):
    """Mark an existing task as REMOVED.  Raise KeyError if not found"""
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    """Remove and return the lowest priority task.  Raise KeyError if empty"""
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


# Dijkstra algorithm
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    @staticmethod
    def construct_graph(nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if not graph[adjacent_node].get(node, False):
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False):
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    while node != start_node:
        path.append(f"{node}")
        node = previous_nodes[node]
    path.append(start_node)
    print(f"We found the following best path with a value of {shortest_path[target_node]}.")
    # print(" -> ".join(reversed(path)))


def dijkstra_algorithm(graph, start_node):
    # unvisited_nodes = []
    shortest_path = {}
    previous_nodes = {}
    shortest_path[start_node] = 0

    max_value = sys.maxsize
    for node in graph.get_nodes():
        if node != start_node:
            shortest_path[node] = max_value
            # unvisited_nodes.append(node)
            previous_nodes[node] = None
        add_task(node, shortest_path[node])

    # while unvisited_nodes:
    while entry_finder:
        current_min_node = pop_task()
        # current_min_node = None
        # for node in unvisited_nodes:
        #     if current_min_node is None:
        #         current_min_node = node
        #     elif shortest_path[node] < shortest_path[current_min_node]:
        #         current_min_node = node

        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            # tentative_value = shortest_path[current_min_node] + graph.value(neighbor, current_min_node)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
                add_task(neighbor, tentative_value)

        # unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_board(board):
    """ Print the board with node costs """
    for r in board:
        print(r)


def new_tile_with_more_risk(arr):
    ones = np.ones_like(arr)
    res = np.empty_like(arr)
    res = np.add(arr, ones)
    for y in range(res.shape[0]):
        for x in range(res.shape[1]):
            while res[x, y] > 9:
                res[x, y] -= 9
    return res


def main_old():
    """ Test Dijkstra's Algorithm code """
    nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

    init_graph = {}
    for node in nodes:
        init_graph[node] = {}

    init_graph["Reykjavik"]["Oslo"] = 5
    init_graph["Reykjavik"]["London"] = 4
    init_graph["Oslo"]["Berlin"] = 1
    init_graph["Oslo"]["Moscow"] = 3
    init_graph["Moscow"]["Belgrade"] = 5
    init_graph["Moscow"]["Athens"] = 4
    init_graph["Athens"]["Belgrade"] = 1
    init_graph["Rome"]["Berlin"] = 2
    init_graph["Rome"]["Athens"] = 2

    graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")
    print_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Belgrade")


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        tile_tmp = []

        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")

            row = []
            for ch in tmp:
                if ch.isdigit():
                    row.append(int(ch))
            tile_tmp.append(row)
        tile = np.array(tile_tmp)
        print(tile, tile.shape)

    tile1 = new_tile_with_more_risk(tile)
    tile2 = new_tile_with_more_risk(tile1)
    tile3 = new_tile_with_more_risk(tile2)
    tile4 = new_tile_with_more_risk(tile3)
    tile5 = new_tile_with_more_risk(tile4)
    tile6 = new_tile_with_more_risk(tile5)
    tile7 = new_tile_with_more_risk(tile6)
    tile8 = new_tile_with_more_risk(tile7)

    row0 = np.concatenate((tile, tile1, tile2, tile3, tile4), axis=1)
    row1 = np.concatenate((tile1, tile2, tile3, tile4, tile5), axis=1)
    row2 = np.concatenate((tile2, tile3, tile4, tile5, tile6), axis=1)
    row3 = np.concatenate((tile3, tile4, tile5, tile6, tile7), axis=1)
    row4 = np.concatenate((tile4, tile5, tile6, tile7, tile8), axis=1)

    board = np.concatenate((row0, row1, row2, row3, row4))
    # board = np.copy(tile)
    print(board, board.shape)

    # Dynamic Programming algorith
    # row_max, col_max = board.shape
    #
    # # build q (cost array)
    # q = np.zeros_like(board)
    # # print(q)
    # q[0, 0] = 0
    # for row_iter in range(1, row_max):
    #     """ Starting at top left of board, move down a row at a time.
    #         From there, move up and right diagonally to top row. """
    #     x, y = 0, row_iter
    #     while x < col_max and y >= 0:
    #         # print(f"{(x,y)}")
    #         m1 = q[y, x-1] if x > 0 else 999999
    #         m2 = q[y-1, x] if y > 0 else 999999
    #         if m1 == 0 or m2 == 0:
    #             print(f"{x,y} touches 0-cost node")
    #         m = min([m1, m2])
    #         q[y, x] = m + board[y, x]
    #         x += 1
    #         y -= 1
    # for col_iter in range(1, col_max):
    #     """ Starting at bottom left of board, move right a column at a time.
    #         From there, move up and right diagonally to last column. """
    #     # print(i)
    #     x, y = col_iter, row_max - 1
    #     while x < col_max and y >= 0:
    #         # print(f"{(x,y)}")
    #         m1 = q[y, x-1] if x > 0 else 999999
    #         m2 = q[y-1, x] if y > 0 else 999999
    #         if m1 == 0 or m2 == 0:
    #             print(f"{x,y} touches 0-cost node")
    #         m = min([m1, m2])
    #         q[y, x] = m + board[y, x]
    #         x += 1
    #         y -= 1
    # print(q)

    # Djikstra's Algorithm
    nodes = []
    for r in range(board.shape[0]):
        for c in range(board.shape[0]):
            nodes.append( (r,c) )

    init_graph = {}
    for node in nodes:
        init_graph[node] = {}

    for r in range(board.shape[0]):
        for c in range(board.shape[1]):
            if r > 0:
                # can move down to this node
                init_graph[(r-1, c)][(r, c)] = board[r, c]
            if r < board.shape[0] - 1:
                # can move up to this node
                init_graph[(r+1, c)][(r, c)] = board[r, c]
            if c > 0:
                # can move right to this node
                init_graph[(r, c-1)][(r, c)] = board[r, c]
            if c < board.shape[1] - 1:
                # can move left to this node
                init_graph[(r, c+1)][(r, c)] = board[r, c]

    graph = Graph(nodes, init_graph)

    start = (0, 0)
    finish = (board.shape[0]-1, board.shape[1]-1)

    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start)
    # print(f"previous_nodes = {previous_nodes}")
    # print(f"shortest path = {shortest_path}")
    print_result(previous_nodes, shortest_path, start_node=start, target_node=finish)


if __name__ == '__main__':
    main()

from helpers.searchgui import *
from queue import Queue

def link_nodes():
    for row in range(50):
        for col in range(75):
            if col > 0:
                node = graph[row][col - 1]
                if node.nodeType != 'obstruct':
                    graph[row][col].neighbors.append(node)
            if col < 74:
                node = graph[row][col + 1]
                if node.nodeType != 'obstruct':
                    graph[row][col].neighbors.append(node)
            if row > 0:
                node = graph[row - 1][col]
                if node.nodeType != 'obstruct':
                    graph[row][col].neighbors.append(node)
            if row < 49:
                node = graph[row + 1][col]
                if node.nodeType != 'obstruct':
                    graph[row][col].neighbors.append(node)

def reconstruct_path(previous, start, current):
    end = current
    while current in previous:
        current = previous[current]
        if current != end and current != start:
            current.makePath()
            color_nodes()

def bfsearch(graph, start, finish):
    link_nodes()

    if start == None or finish == None:
        return False
    
    previous = {}

    visited = [start]
    
    open_set = Queue()
    open_set.put(start)

    while not open_set.empty():
        node = open_set.get()

        if node != start and node != finish:
            node.makeClosed()
            color_node(node.row, node.col)
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                open_set.put(neighbor)
                visited.append(neighbor)
                previous[neighbor] = node

                if neighbor != start and neighbor != finish:
                    neighbor.makeOpen()
                    color_node(neighbor.row, neighbor.col)

                if neighbor == finish:
                    reconstruct_path(previous, start, finish)    
                    color_finished()
                    return True

    return False 
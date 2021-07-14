from helpers.searchgui import *
from queue import PriorityQueue

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

def h(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)

def reconstruct_path(previous, start, current):
    end = current
    while current in previous:
        current = previous[current]
        if current != end and current != start:
            current.makePath()
            color_nodes()
        

def astar_search(graph, start, finish):
    global openNodesList
    
    if start == None or finish == None:
        return False
    
    link_nodes()

    count = 0

    open_set = PriorityQueue()
    open_set.put((0, count, start))
    open_set_hash = {start}

    previous = {}
    
    g_score = {Node: float('inf') for row in graph for Node in row}
    g_score[start] = 0

    f_score = {Node: float('inf') for row in graph for Node in row} 
    f_score[start] = h(start, finish)

    while not open_set.empty():
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current != start and current != finish:
            current.makeClosed()
            color_node(current.row, current.col)
        
        if current == finish:
            reconstruct_path(previous, start, finish)
            finish.makeEnd()
            color_finished()
            return True
        
        for neighbor in current.neighbors:
            temp_g = g_score[current] + 1

            if temp_g < g_score[neighbor]:
                previous[neighbor] = current

                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + h(neighbor, finish)

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.makeOpen()
                    color_node(neighbor.row, neighbor.col)

    return False
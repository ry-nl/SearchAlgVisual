from helpers.searchgui import *

def link_nodes():
    for row in range(50):
        for col in range(75):
            this = graph[row][col]
            if col > 0:
                node = graph[row][col - 1]
                if node.nodeType != 'obstruct':
                    this.links[node] = (this.weight + node.weight)
            if col < 74:
                node = graph[row][col + 1]
                if node.nodeType != 'obstruct':
                    this.links[node] = (this.weight + node.weight)
            if row > 0:
                node = graph[row - 1][col]
                if node.nodeType != 'obstruct':
                    this.links[node] = (this.weight + node.weight)
            if row < 49:
                node = graph[row + 1][col]
                if node.nodeType != 'obstruct':
                    this.links[node] = (this.weight + node.weight)
                    
def generate_dijgraph(graph):
    dijgraph = {}
    for row in graph:
        for node in row:
            dijgraph[node] = node.links
    
    return dijgraph
    
def dijkstra(graph, start, finish):
    global openNodesList

    if start == None or finish == None:
        return False
    link_nodes()
    dijgraph = generate_dijgraph(graph)
    
    # our initially 'infinite' distance
    init_dist = float('inf')
    # where shortest path gets stored
    path = []
    # all nodes in graph are initially unvisited, including start node
    unvisited = dijgraph
    # dictionaries to store shortest distance to and predecessor of each node in the graph
    shortest_distance = {}
    predecessor = {}

    # initialize the distances of unvisited nodes
    for node in unvisited:
        shortest_distance[node] = init_dist
    shortest_distance[start] = 0
    
    # loop through unvisited nodes
    while unvisited:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        # map closest node to current node 
        closestNode = None
        for node in unvisited:
            if closestNode == None:
                closestNode = node
            elif shortest_distance[node] < shortest_distance[closestNode]:
                closestNode = node
        if closestNode != start and closestNode != finish:
            closestNode.makeClosed()
            color_node(closestNode.row, closestNode.col)
            
        # check if current path is shorter than current shortest distance to a given node 
        for child, weight in dijgraph[closestNode].items():
            # if shorter, replace shortest distance and replace predecessor
            if weight + shortest_distance[closestNode] < shortest_distance[child]:
                shortest_distance[child] = weight + shortest_distance[closestNode]
                predecessor[child] = closestNode

            if child != start and child != finish:
                if child in unvisited:
                    child.makeOpen()
                    color_node(child.row, child.col)
        
        # unvisited node is now visited, so pop
        unvisited.pop(closestNode)

        if closestNode == finish:
            break
            
    
    current = finish
    while True:
        # try to insert predecessors into path
        try:
            path.insert(0, current)
            current = predecessor[current]
        except KeyError:
            return False
        # to insert start node in path
        if current == start:
            path.insert(0, current)
            break
        
    # check if goal was reached
    if shortest_distance[finish] != init_dist:
        for node in path:
            if node != start and node != finish:
                node.makePath()
                color_nodes()
                
    color_finished()

    return True
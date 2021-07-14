import helpers.searchgui as sg
import helpers.graph as g
import algorithms.astar as astar
import algorithms.dijkstras as dij
import algorithms.bfs as bfs

def clear():
    for row in g.graph:
        for node in row:
            node.makeNeutral()
            node.links.clear()
            node.neighbors.clear()
            g.startendNodes[0] = None
            g.startendNodes[1] = None
            
previous = None
action = None

while True:
    action = sg.main_loop()

    if action == 'reset':
        previous = None
        clear()
    if action == 'astar' and previous != action:
        previous = 'astar'
        astar.astar_search(g.graph, g.startendNodes[0], g.startendNodes[1])
    if action == 'dijkstras' and previous != action:
        previous = 'dijkstras'
        dij.dijkstra(g.graph, g.startendNodes[0], g.startendNodes[1])
    if action == 'bfs' and previous != action:
        previous = 'bfs'
        bfs.bfsearch(g.graph, g.startendNodes[0], g.startendNodes[1])
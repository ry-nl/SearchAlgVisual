from helpers.node import *
from math import sqrt, pow

graph = [[None] * 75 for i in range(50)]

for row in range(50):
    for col in range(75):
        graph[row][col] = Node((100 + row * 5, col * 5), (row, col))
        
startendNodes = [None, None]
path = []

def getDistance(node1, node2):
    if node1 == node2:
        return 0
    
    distance = abs(sqrt(pow((node1.x + node2.x), 2), pow((node1.y, node2.y), 2)))
    return distance

def dk_linkNodes(node1, node2):
    if node1 != node2:
        distance = getDistance(node1, node2)
        node1.links[node2] = distance
        node2.links[node1] = distance
    else:
        print('nodes could not be linked')


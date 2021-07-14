import threading
import time

class Node:
   
    obstructColor = '#333333'
    pathColor = '#F7F37E'
    startColor = '#FFD176'
    endColor = '#FF9376'
    neutralColor = '#EEEEEE'
    openColor = '#92F884'
    closedColor = '#7EE38E'
    finishColor = '#76E7FF'
    
    def __init__(self, location, coordinates):
        self.x = location[0]
        self.y = location[1]
        self.row = coordinates[0]
        self.col = coordinates[1]
        self.path = False
        
        self.weight = 1
        
        self.links = {}
        self.neighbors = []
        
        self.makeNeutral()
    
    def makeObstruct(self):
        self.nodeType = 'obstruct'
        self.color = self.obstructColor
        self.weight = 1
        
    def makePath(self):
        self.nodeType = 'path'
        self.color = self.pathColor
        
    def makeStart(self):
        self.nodeType = 'start'
        self.color = self.startColor
        self.weight = 1
        
    def makeEnd(self):
        self.nodeType = 'end'
        self.color = self.endColor
        self.weight = 1

    def makeNeutral(self):
        self.nodeType = 'neutral'
        self.color = self.neutralColor
        self.weight = 1
    
    def makeOpen(self):
        self.nodeType = 'open'
        self.color = self.openColor
    
    def makeClosed(self):
        self.nodeType = 'closed'
        self.color = self.closedColor

    def makeFinished(self):
        self.nodeType = 'finished'
        self.color = self.finishColor
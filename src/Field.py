'''
Created on Dec 23, 2018

@author: Ian
'''
from Cell import *


class Field(object):
    
    global patterns
    patterns = {"block": ((1, 1), (1, 1)), "blinker": ((0, 0, 0), (1, 1, 1), (0, 0, 0)),
                "glider": ((0,1,0),(0,0,1),(1,1,1))}

    def __init__(self, x, y):
        self.space = [[Cell(i, j, 0) for i in range(y)] for j in range (x)]
        self.size = (len(self.space), len(self.space[0]))
    
    def neighbors(self):
        "Returns a matrix with number of neighbors as entries" 
        neighbors = [[0 for i in range(self.size[1])] for j in range(self.size[0])]
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                total = 0
                try:
                    total += self.space[x][y + 1].life
                except Exception:
                    pass
                try:
                    total += self.space[x + 1][y + 1].life 
                except Exception:
                    pass
                try:
                    total += self.space[x + 1][y].life
                except Exception:
                    pass
                try:
                    total += self.space[x + 1][y - 1].life  
                except Exception:
                    pass
                try: 
                    total += self.space[x][y - 1].life
                except Exception:
                    pass
                try:
                    total += self.space[x - 1][y - 1].life
                except Exception:
                    pass
                try:
                    total += self.space[x - 1][y].life
                except Exception:
                    pass
                try:
                    total += self.space[x - 1][y + 1].life
                except Exception:
                    pass
                
                neighbors[x][y] = total
        return neighbors
    
    def healthypop(self, neighbors):
        if neighbors == 2 or neighbors ==3 :
            return 1
        else: 
            return 0
    
    def birth(self, neighbors):
        if neighbors == 3:
            return 1
        else:
            return 0
    
    def nextgen(self):
        neighbors = self.neighbors()
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                
                if self.space[x][y].life == 1:
                    "check for healthy population"
                    self.space[x][y].life = self.healthypop(neighbors[x][y])
        
                else:
                    "check for birth"
                    self.space[x][y].life = self.birth(neighbors[x][y])
            
    def create(self, pattern, x, y):
        for j in range(len(patterns[pattern])):
            for i in range(len(patterns[pattern][0])):
                self.space[x + j][y + i].life = patterns[pattern][i][j]
            

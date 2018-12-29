'''
Created on Dec 23, 2018

@author: Ian
'''


class Cell(object):

    def __init__(self, x, y, life):
        self.position = (x, y)
        self.life = life
    
    def death(self):
        self.life = 0
    
    def life(self):
        self.life = 1

        

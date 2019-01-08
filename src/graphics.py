'''
Created on Dec 26, 2018

@author: Ian
'''
import pygame


class Window(object):
    
    global colors
    colors = {"white" : (255, 255, 255), "black": (0, 0, 0) }

    def __init__(self, width, height):
        self.size = width, height
        
    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        
    def drawcell(self, x , y):
        pygame.draw.rect(self.screen, colors["white"], (x, y, 4, 4), 0)
    
    def erasecell(self, x , y):
        pygame.draw.rect(self.screen, colors["black"], (x, y, 4, 4), 0)
        
    def draw(self, field):
        for i in range(field.size[0]):
            for j in range(field.size[1]):
                if field.space[i][j].life == 1:
                    self.drawcell(i * 4, j * 4)
                else:
                    self.erasecell(i * 4, j * 4)
             
            

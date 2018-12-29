'''
Created on Dec 24, 2018

@author: Ian
'''
from Field import Field
from Window import *
import sys

field = Field(100, 100)

field.create("block", 50, 10)
field.create("glider", 0, 0)
field.create("blinker", 70,70)

window = Window(field.size[0] * 4, field.size[1] * 4)
window.initialize()
window.draw(field)
pygame.display.update()
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
    field.nextgen()
    window.draw(field)
    pygame.display.update()

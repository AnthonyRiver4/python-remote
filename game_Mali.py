#import the pygame module, and the
#sys module for exiting the window we create
import pygame, sys

#import some useful constants
from pygame.locals import *

#color constants
black = (0,0,0)

#cloud
c1 = (247,247,247)
c2 = (223,223,223)
c3 = (191,191,191)

#building
b1 = (222,184,135)
b2 = (210, 156, 87)
b3 = (205,133,63)
b4 = (151, 103, 41)

#wood
w1 = (171, 112, 83)
w2 = (131, 84, 63)
w3 = (91,57,43)

#sky
s1 = (149, 204, 222)

#
#Enter game code here
#
#
#

#initialize the pygame module
pygame.init()

#create a new drwing surface, width = 500, length = 500
DISPLAYSURF= pygame.display.set_mode((500,500))

#give the window a caption
pygame.display.set_caption('The Great Mosque of Djenne')

# loop to repeat infinitely
while True:
    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #ennd the game and close the window
            pygame.quit()
            sys.exit()

    #DRAW GAME CODE
    #background
    pygame.draw.rect(DISPLAYSURF, (b1),(0,250,500,500))
    pygame.draw.rect(DISPLAYSURF, (s1),(0,0,500,250))
    
    #main building
    pygame.draw.rect(DISPLAYSURF, (b2),(110,200,280,200))
    pygame.draw.rect(DISPLAYSURF, (black),(245,370,15,30))
    
    #side sites
    pygame.draw.rect(DISPLAYSURF, (b3),(70,370,100,50))
    pygame.draw.rect(DISPLAYSURF, (b3),(330,370,100,50))
    
    #outer wall
    pygame.draw.rect(DISPLAYSURF, (b4),(20,390,460,50))
  

    #update the display
    pygame.display.update()
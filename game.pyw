import pygame as pg
import math
import random


#Actual window size
windowY = 600
windowX = 800

screenX = 1000

pg.init()
window = pg.display.set_mode((windowX, windowY))
clock = pg.time.Clock()
pg.display.set_caption('')


def makeObject(x, y, x2, y2, img, path):  #if "img" = True, "path" must be img path. If "img" = False, path must be rgb   
    side1 = (x, y, y2, "right")
    side2 = (x2, y, y2, "left")
    walls.append(side1)
    walls.append(side2)
    top = (x, y, x2)
    platforms.append(top)
    bottom = (x, y2, x2)
    roofs.append(bottom)
    all = (x, y, x2, y2, img, path)
    visualObjects.append(all)


#Walls here              (X1,Y1,Y2, Where the depth goes to)
leftSide = (0, 0, windowY, "left")
rightSide = (screenX, 0, windowY, "right")
#wall = (400, 200, windowY, "right")

walls = [leftSide, rightSide]

#Grounds here            (X1,Y1,X2)
ground = (0, windowY, screenX)

platforms = [ground]

#Roofs here              (X1, Y1, X2)
roof = (0, 0, screenX)

roofs = [roof]


visualObjects = []


#Make Objects here

makeObject(100, 100, 120, windowY, False, (0,0,0))
makeObject(100, 100, screenX - 100, 120, False, (0,0,0))
makeObject(screenX - 120, 100, screenX - 100, windowY - 100, False, (0,0,0))
for x in range(0, 10):
    makeObject(120, 200 + (50 * x), 140, 220 + (50 * x), False, (0,0,0))
makeObject(200, windowY - 150, screenX - 101, windowY - 130, False, (0,0,0))


def eventLoop():
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                quit()
        if event.type == pg.QUIT:
            quit()
                

from player import *

def game():
    x = player.x - player.width / 2 - windowX / 2
    if x < 0:
        x = 0
    elif x + windowX > screenX:
        x = screenX - windowX
        
    try:
        tick += 1
    except:
        tick = 0
            

    window.fill((255,255,255))

    for img in visualObjects:
        if img[4]:
            blitImg = pg.transform.scale(img[5], (img[2] - img[0], img[3] - img[1]))
            window.blit(blitImg, (img[0] - x, img[1]))
        else:
            pg.draw.rect(window, img[5], (img[0] - x, img[1], img[2] - img[0], img[3] - img[1]))

               
        
    eventLoop()
    playerBlitInfo = player.update()
    window.blit(playerBlitInfo[0], (playerBlitInfo[1] - x, playerBlitInfo[2]))
        
    pg.display.update()
    clock.tick(60)

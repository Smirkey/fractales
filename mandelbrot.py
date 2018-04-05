import pygame
import numpy as np
from pygame.locals import *
from PIL import Image
import pygame.mouse as mouse
windowX = 500
windowY = 500
max_iters = 1000
scaleX = [-2, 2]
scaleY = [-2, 2]
mouseJustGotPressed = False
def toImage(grid):
    print(grid)
    newGrid = np.zeros(shape=(grid.shape[0], grid.shape[1]))

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == 0:
                newGrid[i][j] = 0
            else:
                #newGrid[i][j] = map(grid[i][j], 0, max_iters, 0, 255)
                newGrid[i][j] = 255
    print("conversion done")            
    return newGrid


def iter(grid , x, y):
    newGrid = np.zeros(shape=(grid.shape[0], grid.shape[1]))
    for i in range(grid.shape[0]):

        if i%(grid.shape[0]/100) == 0:
            print("{} % done".format(map(i, 0, grid.shape[0], 0, 100)))
        for j in range(grid.shape[1]):
            a = map(i, 0, grid.shape[0], x[0], x[1])
            b = map(j, 0, grid.shape[1], y[0], y[1])
            z = 0
            orA = a
            orB = b
            for k in range(max_iters):
                new_a = a*a - b*b
                new_b = 2*a*b
                a = new_a + orA
                b = new_b + orB
                if abs(a + b) > 16:
                    newGrid[i][j] = k
                    break

    return newGrid


def map(n, xStart, yStart, xTarget, yTarget):
    return xTarget + n/(yStart + xStart)*(yTarget - xTarget)


def show(grid):
    surf = pygame.surfarray.make_surface(grid)
    window.blit(surf, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
def zoom():
    mousePressed = mouse.get_pressed()[0]
    if mousePressed == 0:
            firstPress = True
    if mousePressed:
        print(firstPress)
        if firstPress:
            initialPos = mouse.get_pos()
            firstPress = False
        mousePos = mouse.get_pos()
        print(initialPos, mousePos)
        pygame.draw.rect(surf, 255, (initialPos[0], initialPos[1], mousePos[0], mousePos[1]), 1)



Grid = np.zeros(shape=(windowX, windowY))
Grid = iter(Grid, scaleX, scaleY)
image = toImage(Grid)
surf = pygame.surfarray.make_surface(image)
pygame.image.save(surf, "output.png")
pygame.init()
window = pygame.display.set_mode((windowX,windowY))
firstPress = True
initialPos = (0,0)
rX = 0
rY = 0
while 1:
    mousePressed = mouse.get_pressed()[0]
    surf = pygame.surfarray.make_surface(image)
    if mousePressed:
        mouseJustGotPressed = True
        if firstPress:
            initialPos = mouse.get_pos()
            firstPress = False
            rX = 0
            rY = 0
        mousePos = mouse.get_pos()
        pygame.draw.rect(surf, 0, (initialPos[0], initialPos[1], rX, rY), 1)
        rel = mouse.get_rel()
        rX += rel[0]
        rY += rel[1]
    window.blit(surf, (0, 0))
    pygame.display.flip()
    if mousePressed == 0:
        firstPress = True
        rel = mouse.get_rel()
        if mouseJustGotPressed:
            print(initialPos[0],initialPos[0] + rX)
            scaleX = [map(initialPos[0], 0, windowX, scaleX[0], scaleX[1]), map(initialPos[0] + rX, 0, windowX, scaleX[0], scaleX[1])]
            scaleY = [map(initialPos[1], 0, windowY, scaleY[0], scaleY[1]), map(initialPos[1] + rY, 0, windowY, scaleY[0], scaleY[1])]
            scaleX.sort()
            scaleY.sort()

            Grid = np.zeros(shape=(windowX, windowY))
            Grid = iter(Grid, scaleX, scaleY)
            image = toImage(Grid)
            surf = pygame.surfarray.make_surface(image)
            mouseJustGotPressed = False


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

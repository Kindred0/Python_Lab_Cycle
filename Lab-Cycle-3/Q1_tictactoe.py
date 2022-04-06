from turtle import width
import pygame, sys
from pygame.locals import *

pygame.init()

class X_sprite:
    def __
    pygame.draw.line

state = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0],
]

player = 1

screen=pygame.display.set_mode([440,680])
screen.fill((255,255,255))
y=20
for i in range(0,3):
    x=20
    for j in range(0,3):
        pygame.draw.rect(screen,(125,125,125),(x,y,120,120))
        x=x+140
    y=y+140

pygame.draw.rect(screen,(0,0,0),(20,440,400,100),5)
pygame.draw.rect(screen,(150,150,150),(60,560,320,100))
pygame.draw.rect(screen,(75,75,75),(60,560,320,100),2)
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < 540 and pos[1] > 340:
                pygame.quit()
                sys.exit()
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            sys.exit()
    pygame.display.update()

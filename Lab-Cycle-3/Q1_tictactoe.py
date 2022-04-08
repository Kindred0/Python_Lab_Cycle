
import pygame, sys
from pygame.locals import *

pygame.init()

def drawXorO(player, posx, posy) :
    if player == 1 :
        pygame.draw.line(screen, (0, 0, 0), (posx+20, posy+20), (posx+80, posy+80), 10)
        pygame.draw.line(screen, (0, 0, 0), (posx+80, posy+20), (posx+20, posy+80), 10)
    elif player == -1 :
        pygame.draw.circle(screen, (0, 0, 0), (posx+50, posy+50), 35, 8)
state = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
    ]

XWon = pygame.image.load('X_WON.png')
OWon = pygame.image.load('O_WON.png')
Reset = pygame.image.load('RESET.png')

def drawVicotry(player):
    if player == 1 :
        screen.blit(XWon, (25, 400))
    if player == -1 :
        screen.blit(OWon, (25, 400))




player = 1
win = False

screen=pygame.display.set_mode([400, 600])
screen.fill((255, 255, 255))
pygame.display.set_caption('TIC TAC TOE')
y = 25
for i in range(0, 3):
    x = 25
    for j in range(0, 3):
        pygame.draw.rect(screen, (125, 125, 125),(x, y, 100, 100))
        x = x + 125
    y = y + 125

pygame.draw.rect(screen, (0, 0, 0), (25, 400, 350, 75), 5)
pygame.draw.rect(screen, (150, 150, 150), (60, 500, 280, 75))
pygame.draw.rect(screen, (75, 75, 75), (60, 500, 280, 75), 2)
screen.blit(Reset, (90, 500))
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            y = 25
            for i in range(0, 3) :
                x = 25
                for j in range(0, 3) :
                    if pos[0] > x and pos[1] > y and pos[0] < x + 100 and pos[1] < y + 100 and state[i][j] == 0 and win == False :
                        drawXorO(player, x, y)
                        state[i][j] = player
                        player = player * -1
                    x = x +125
                y = y + 125

            #reset button code
            if pos[0] > 60 and pos[1] > 500 and pos[0] < 340 and pos[1] < 575 :
                y = 25
                for i in range(0, 3) :
                    x = 25
                    for j in range(0, 3) :
                        pygame.draw.rect(screen, (125, 125, 125),(x, y, 100, 100))
                        x = x + 125
                    y = y + 125
                state = [
                    [0, 0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0]
                    ]
                pygame.draw.rect(screen, (255, 255, 255), (25, 400, 350, 75))
                pygame.draw.rect(screen, (0, 0, 0), (25, 400, 350, 75),5)
                win = False
                player = 1


        for i in state :
            sum = 0
            for j in i :
                sum = sum + j
            if sum == 3 :
                drawVicotry(1)
                win = True
            if sum == -3 :
                drawVicotry(-1)
                win = True     
        
        for j in range(0, 3) :
            sum = 0
            for i in state :
                sum = sum + i[j]
            if sum == 3 :
                drawVicotry(1)
                win = True
            if sum == -3 :
                drawVicotry(-1)
                win = True
        
        sum = 0
        for i in range(0, 3) :
            sum = sum + state[i][i]
        if sum == 3 :
            drawVicotry(1)
            win = True
        if sum == -3 :
            drawVicotry(-1)
            win = True
        
        sum = 0
        for i in range( 0, 3) :
            sum = sum +state[i][2-i]
        if sum == 3 :
            drawVicotry(1)
            win = True
        if sum == -3 :
            drawVicotry(-1)
            win = True                            

        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            sys.exit()
    pygame.display.update()
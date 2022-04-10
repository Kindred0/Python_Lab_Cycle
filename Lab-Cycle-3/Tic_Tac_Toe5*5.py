
import pygame, sys
from pygame.locals import *

pygame.init()

def drawXorO(player, posx, posy) :
    if player == 1 :
        pygame.draw.line(screen, (0, 0, 0), (posx+2.5, posy+2.5), (posx+22.5, posy+22.5), 3)
        pygame.draw.line(screen, (0, 0, 0), (posx+22.5, posy+2.5), (posx+2.5, posy+22.5), 3)
    elif player == -1 :
        pygame.draw.circle(screen, (0, 0, 0), (posx+12.5, posy+12.5), 10, 2)

state = []
for i in range(0,15) :
    state.append([])
    for j in range(0,15) :
        state[i].append(0)

XWon = pygame.image.load('X_WON.png')
OWon = pygame.image.load('O_WON.png')
Reset = pygame.image.load('RESET.png')

def drawVicotry(player):
    if player == 1 :
        screen.blit(XWon, (50, 455))
    if player == -1 :
        screen.blit(OWon, (50, 455))




player = 1
win = False

screen=pygame.display.set_mode([455, 655])
screen.fill((255, 255, 255))
pygame.display.set_caption('TIC TAC TOE')
y = 5
for i in range(0, 15):
    x = 5
    for j in range(0, 15):
        pygame.draw.rect(screen, (125, 125, 125),(x, y, 25, 25))
        x = x + 30
    y = y + 30

pygame.draw.rect(screen, (0, 0, 0), (50, 455, 355, 75), 5)
pygame.draw.rect(screen, (150, 150, 150), (100, 555, 255, 75))
pygame.draw.rect(screen, (75, 75, 75), (100, 555, 255, 75), 2)
screen.blit(Reset, (115, 555))
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            y = 5
            for i in range(0, 15) :
                x = 5
                for j in range(0, 15) :
                    if pos[0] > x and pos[1] > y and pos[0] < x + 25 and pos[1] < y + 25 and state[i][j] == 0 and win == False :
                        drawXorO(player, x, y)
                        state[i][j] = player
                        player = player * -1
                    x = x +30
                y = y + 30

            #reset button code
            if pos[0] > 100 and pos[1] > 555 and pos[0] < 355 and pos[1] < 630 :
                y = 5
                for i in range(0, 15) :
                    x = 5
                    for j in range(0, 15) :
                        pygame.draw.rect(screen, (125, 125, 125),(x, y, 25, 25))
                        x = x + 30
                    y = y + 30
                state = []
                for i in range(0,15) :
                    state.append([])
                    for j in range(0,15) :
                        state[i].append(0)

                pygame.draw.rect(screen, (255, 255, 255), (50, 455, 355, 75))
                pygame.draw.rect(screen, (0, 0, 0), (50, 455, 355, 75),5)
                win = False
                player = 1

        present = 0
        for i in state :
            sum = 0
            for j in i :
                if present == j :
                    sum = sum + j
                else :
                    present = j
                    sum = j
                if sum == 5 :
                    drawVicotry(1)
                    win = True
                if sum == -5 :
                    drawVicotry(-1)
                    win = True     
        
        present = 0
        for j in range(0, 15) :
            sum = 0
            for i in state :
                if present == i[j] :
                    sum = sum + i[j]
                else :
                    present = i[j]
                    sum = i[j]
                if sum == 5 :
                    drawVicotry(1)
                    win = True
                if sum == -5 :
                    drawVicotry(-1)
                    win = True
        
        present = 0
        i = 14
        while i >= 0 :
            sum = 0
            for k in range(0, 15 - i) :
                m = i
                if present == state[m][k] :
                    sum = sum + state[m][k]
                else :
                    present = state[m][k]
                    sum = state[m][k]
                m = m + 1
                if sum == 5 :
                    drawVicotry(1)
                    win = True
                if sum == -5 :
                    drawVicotry(-1)
                    win = True
            i = i - 1 
        
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
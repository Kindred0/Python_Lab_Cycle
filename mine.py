import pygame
import random
from pygame.locals import *


state = []
for i in range(0,15) :
   	 state.append([])
   	 for j in range(0,15) :
       		 state[i].append(0)

mines = 25

Fail = false

while mines != 0 :
	x = random.randint(0,14)
	y = random.randint(0,14)
	if state[x][y] != -1 :
		state[x][y] = -1
		mines = mines - 1
		if x == 1 :
			for i in range(y,y+2) :
				for k in range(x,x+3) :
					if state[x][y] != -1 :
						state[x][y] = state[x][y] + 1
		elif y == 1 :
			for i in range(y,y+3) :
                                for k in range(x,x+2) :
                                        if state[x][y] != -1 :
                                                state[x][y] = state[x][y] + 1
		elif x == 1 and y == 1 :
			for i in range(y,y+2) :
                                for k in range(x,x+2) :
                                        if state[x][y] != -1 :
                                                state[x][y] = state[x][y] + 1
		else :
			for i in range(y,y+3) :
                                for k in range(x,x+3) :
                                        if state[x][y] != -1 :
                                                state[x][y] = state[x][y] + 1

print(state)

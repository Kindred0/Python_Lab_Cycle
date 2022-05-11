
import random
import pygame

pygame.init()

def ConstructGame() :
	state = []
	for i in range(0,15) :
		state.append([])
		for j in range(0,15) :
				state[i].append(0)

	mines = 30
	# mines represents the number of mines

	Fail = False
	# Fail represents the winning state


	while mines != 0 :
		x = random.randint(0,14)
		y = random.randint(0,14)
		if state[x][y] != -1 :
			state[x][y] = -1
			mines = mines - 1

			if x == 0 and y == 0 :
				for i in range(0,2) :
					for k in range(0,2) :
						if state[i][k] != -1 :
							state[i][k] = state[i][k] + 1

			elif x == 0 and y == 14 :
				for i in range(0,2) :
					for k in range(13,15) :
						if state[i][k] != -1 :
							state[i][k] = state[i][k] + 1
			
			elif x == 14 and y == 0 :
				for i in range(13,15) :
					for k in range(0,2) :
						if state[i][k] != -1 :
							state[i][k] = state[i][k] + 1
			
			elif x == 14 and y == 14 :
				for i in range(13,15) :
					for k in range(13,15) :
						if state[i][k] != -1 :
							state[i][k] = state[i][k] + 1

			elif x == 0 and y != 0 and y != 14 :
				for i in [x,x+1] :
					for k in [y-1,y,y+1] :
						if state[i][k] != -1 :
							state[i][k] = state[i][k] + 1
			elif y == 0 and x != 0  and x != 14 :
				for i in [x-1,x,x+1] :
					for k in [y,y+1] :
						if state[i][k] != -1 :
							state[i][k] = state[i][k] + 1

			elif x == 14 and y != 0 and y != 14 :
				for i in [x-1,x] :
					for k in [y-1,y,y+1] :
						if state[i][k] != -1 :
							state[i][k] = state[i][k] + 1
			

			elif y == 14  and x != 0 and x != 14:
				for i in [x-1,x,x+1] :
					for k in [y-1,y] :
						if state[i][k] != -1 :
							state[i][k] = state[i][k] + 1
			
			else :
				for i in [x-1,x,x+1] :
					for k in [y-1,y,y+1] :
						if state[i][k] != -1 :
							state[i][k] = state[i][k] + 1

	return state


State = ConstructGame()
for i in State : 
	for j in i :
		print(j,"\t",end = "")
	print(" ")

screen = pygame.display.set_mode([455, 655])
screen.fill(255,255,255)
pygame.display.set_caption('Mine Sweeper')
y = 5
for i in range(0, 15):
    x = 5
    for j in range(0, 15):
        pygame.draw.rect(screen, (125, 125, 125),(x, y, 25, 25))
        x = x + 30
    y = y + 30

running = True

while running :
	if event.type == pygame.QUIT :
        running = False
        pygame.quit()
        sys.exit()
    pygame.display.update()
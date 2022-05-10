
import random



state = []
for i in range(0,15) :
   	 state.append([])
   	 for j in range(0,15) :
       		 state[i].append(0)

mines = 25

Fail = False

while mines != 0 :
	x = random.randint(0,14)
	y = random.randint(0,14)
	if state[x][y] != -1 :
		state[x][y] = -1
		mines = mines - 1
		if x == 0 :
			for i in range(y,y+2) :
				for k in range(x-1,x+2) :
					if state[i][k] != -1 :
						state[i][k] = state[i][k] + 1
		elif y == 0 :
			for i in range(y-1,y+2) :
                for k in range(x,x+2) :
                    if state[i][k] != -1 :
                        state[i][k] = state[i][k] + 1
		
		elif x == 0 and y == 0 :
			for i in range(y,y+2) :
                for k in range(x,x+2) :
                    if state[i][k] != -1 :
                        state[i][k] = state[i][k] + 1
		else :
			for i in range(y,y+3) :
                for k in range(x,x+3) :
                    if state[i][k] != -1 :
                        state[i][k] = state[i][k] + 1

print(state)

n=int(input())
last=0
mv=2**n-1
h=[[99,*range(1,n+1)[::-1]],[99],[99]]

def move(f,t):
	print(f+1,t+1)
	h[t].append(h[f].pop())
	global last
	last = h[t][-1]

def legal(f,t):	return h[f][-1]!=last and h[f][-1]!=99 and (h[f][-1]%2!=h[t][-1]%2 or h[t][-1]==99) and h[f][-1]<h[t][-1]

print(mv)
move(0,2) if n%2==1 else move(0,1)

for _ in range(mv-1):
	possibleMoves = list([x,y] for x in range(3) for y in range(3) if x!=y)
	legalMoves = [[f,t] for f,t in possibleMoves if legal(f,t)]
	nextMove = legalMoves[0]
	if len(legalMoves) > 1:
		for m in legalMoves:
			if h[m[1]][-1]!=99: 
				nextMove=m
				break
	move(*nextMove)
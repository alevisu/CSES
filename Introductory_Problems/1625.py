grid,moves=[x==11 or x//9 in [0,8] or x%9 in [0,1] for x in range(1,82)],{'D':+9,'L':-1,"U":-9,"R":+1}

def pGrid(pos):
	for x in range(81):
		c='x ' if (grid[x]) else '- '
		if x==pos: c='\033[91mo \033[0m'
		if x%9==0 and x!=0: print()
		print(c, end='')
	print()

def move(pIndex, pos):
	if pIndex==48 or pos==64: return 1 if pIndex==48 else 0
	if grid[pos-9]==grid[pos+9] and grid[pos-1]==grid[pos+1]: return 0
	grid[pos],r=True,0
	for step in [moves[path[pIndex]]] if path[pIndex] != '?' else moves.values():
		if not grid[pos+step]: r+=move(pIndex+1, pos+step)
	grid[pos]=False;return r

path=input()
print(move(0,10))
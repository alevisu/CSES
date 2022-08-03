def solve(n):
	alive, dead, start = list(range(1,n+1)), [], False
	while len(alive): 
		victims = alive[(start+1)%2::2]
		alive = alive[(start)%2::2]
		dead += victims
		if (len(alive)+len(victims))%2: start = not start
	print(" ".join(map(lambda x:str(x), dead)))

solve(int(input()))
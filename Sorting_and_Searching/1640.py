try:import dotenv,sys;sys.stdin=open('in.txt','r')
except:pass

def solve(n,x,a):
	comps = {}
	for i in range(n):
		c = x - a[i]
		if c in comps: return f"{i+1} {comps[c]}"
		comps[a[i]] = i+1
	return "IMPOSSIBLE"

print(solve(*map(int,input().split()),[*map(int,input().split())]))
def solve():
	n,m=MIIS(I())
	x=[int(x) for x in I().split()]
	swaps=[MIIS(l) for l in sys.stdin.readlines()]

	p,s=[-1]*(n+1)+[1<<24],1
	for i in range(n): p[x[i]]=i
	for i in range(1,len(p)): s+=p[i]<p[i-1] 

	for a,b in swaps:
		a,b=a-1,b-1
		pois=set([x[a],x[a]+1,x[b],x[b]+1])
		for i in pois: s-=p[i]<p[i-1]
		p[x[a]],p[x[b]]=p[x[b]],p[x[a]]
		x[a],x[b]=x[b],x[a]
		for i in pois: s+=p[i]<p[i-1]
		print(s)




# source of cringe, don't watch below this line!
import sys

LOCAL = False
try: 
	sys.stdin=open('in.txt','r')
	# sys.stdout=open('out.txt', 'w')
	LOCAL = True
	def log(*a): print(*a,file=sys.stderr)
	from time import time
	start = time()
except FileNotFoundError:	
	pass

I=input
MIIS=lambda x:map(int,x.split())

solve()

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
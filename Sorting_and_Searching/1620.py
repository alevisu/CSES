def solve(n, target, times):
	lo,	hi = 0, int(1e9 * 1e9)	
	answer = hi
	while lo <= hi:
		time, products = (hi + lo)//2, 0
		for t in times: products += time//t
		if products >= target:
			answer = time
			hi = time-1
		else: lo = time+1
	print(answer)



# source of cringe, don't watch below this line!
import sys

LOCAL = False


try: 
	sys.stdin=open('in.txt','r')
	# sys.stdout=open('out.txt', 'w')
	# sys.stdout=open('/dev/null', 'w')
	LOCAL = True
	def log(*a,**kwa): print(*a,**kwa,file=sys.stderr)
	from time import time
	start = time()
except FileNotFoundError:	
	pass

I=input
MIIS=lambda:[*map(int,I().split())]

solve(*MIIS(), MIIS())

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
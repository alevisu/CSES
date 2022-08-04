def solve(ranges):
	result = ['0'] * N * 2

	ranges.sort(key=lambda x: (x[1], -x[2]))

	HRB = 0
	for r in ranges:
		if r[2] <= HRB: result[r[0]+N] = '1'; continue
		HRB = max(HRB, r[2])
	
	LRB = int(1e9 + 10)
	for r in reversed(ranges):
		if r[2] >= LRB: result[r[0]] = '1'; continue
		LRB = min(LRB, r[2])
	
	print(' '.join(result))


# source of cringe, don't watch below this line!
import sys

LOCAL = False


try: 
	sys.stdin=open('in.txt','r')
	# sys.stdout=open('out.txt', 'w')
	sys.stdout=open('/dev/null', 'w')
	LOCAL = True
	def log(*a,**kwa): print(*a,**kwa,file=sys.stderr)
	from time import time
	start = time()
except FileNotFoundError:	
	pass

I=input
MIIS=lambda:[*map(int,I().split())]

N = int(I())
solve([(id, *MIIS()) for id in range(N)])

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
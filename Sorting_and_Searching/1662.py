from collections import defaultdict


def solve(n, array):
	answer, rt = 0, 0
	seen = defaultdict(int, {0:1})
	for i in array:
		rt = ((rt + i) % n + n) % n
		answer += seen[rt]
		seen[rt] += 1
	print(answer)


# source of cringe, don't watch below this line!
import sys

LOCAL = False


log = lambda*a,**kwa:None
try: 
	sys.stdin=open('ein.txt','r')
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

N = int(I())
solve(N, MIIS())

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
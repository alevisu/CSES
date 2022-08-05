from collections import defaultdict


def solve(target, array):
	answer, rt = 0, 0
	seen = defaultdict(int, {0:1})
	for i in array:
		rt += i 
		answer += seen[rt-target]
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

N, X = MIIS()
solve(X, MIIS())

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
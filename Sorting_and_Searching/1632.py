from bisect import bisect

def solve(k, movies):
	watchers = k*[0]
	movies.sort(key=lambda x: -x[1])
	total = 0
	while movies:
		m = movies.pop()
		wi = bisect(watchers, -m[0], key=lambda x: -x)
		if wi < len(watchers):
			watchers = [m[1]]+watchers[:wi]+watchers[wi+1:]
			total += 1
	print(total)


# source of cringe, don't watch below this line!
import sys

LOCAL = False


log = lambda*a,**kwa:None
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

N, K = MIIS()
solve(K, [(int(a), int(b)) for a, b in (line.split() for line in sys.stdin.readlines())])

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
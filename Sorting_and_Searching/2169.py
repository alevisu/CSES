from math import ceil, log2


class Tree:
	def __init__(self, values):
		self.m, i = {}, 1
		m = self.m
		self.size = 1 << ceil(log2(N))
		m[0] = 0
		for v in values:
			m[v] = i # we need only right values
			i += 1
		self.clear()
		m[N+1] = self.size-1
	
	def clear(self):
		self.d = [0] * 2 * self.size

	def sum(self, l, r): # interval [l, r] (including r)
		l = self.m[l] + self.size
		r = self.m[r] + self.size + 1
		rv, d = 0, self.d
		while l < r:
			if l&1: rv+=d[l]; l+=1
			if r&1: r-=1; rv+=d[r]
			l >>= 1; r >>= 1
		return rv

	def add(self, value):
		i = self.size + self.m[value]
		while i > 0:
			self.d[i] += 1
			i >>= 1


def solve(ranges):
	result = [0] * N * 2

	ranges.sort(key=lambda x: (x[1], -x[2]))
	t = Tree(sorted({x[2] for x in ranges}))

	for r in ranges:
		result[r[0]+N] = t.sum(r[2], N+1)
		t.add(r[2])
	
	t.clear()
	for r in reversed(ranges):
		result[r[0]] = t.sum(0, r[2])
		t.add(r[2])
	
	print(' '.join(str(x) for x in result))


# source of cringe, don't watch below this line!
import sys

LOCAL = False


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

Z = int(1e9 + 10)
N = int(I())
solve([(id, *MIIS()) for id in range(N)])

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
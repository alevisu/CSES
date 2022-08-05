from math import ceil, log2

INF = int(1e9+10)

class MinTree:
	def __init__(self, array):
		self.size = 1 << ceil(log2(len(array)))
		self.d = [0]*self.size + array + [INF]*(self.size-len(array))
		for i in range(self.size-1, 0, -1):
			self.d[i] = min(self.d[i<<1], self.d[1+(i<<1)])

	def findLesserThan(self, bigger):
		i, d = bigger + self.size, self.d
		biggerValue = d[i]
		if self.findMinInRange(0, bigger) >= biggerValue: return 0
		
		# we can go only left and left-up until we find lesser number
		# after that - just have to find minimum from current node
		while d[i] >= biggerValue:
			if i&1: i >>= 1 #if we in right node - jump left-up
			else: i -= 1 #else just jump left
		while i < self.size:
			i <<= 1 #jump left-down
			if d[i+1] < biggerValue: i += 1 # if right node is ok - jump to it

		return i - self.size + 1

	def findMinInRange(self, l, r):
		l, r, d = l+self.size, r+self.size, self.d
		rv = INF
		while l<r:
			if l&1: rv = min(rv, d[l]); l += 1
			if r&1: r -= 1; rv = min(rv, d[r])
			l >>= 1; r >>= 1
		return rv
				

def solve(array):
	t = MinTree(array)
	for bigger in range(len(array)):
		print(t.findLesserThan(bigger), end=' ', flush=False)
	sys.stdout.flush()


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
MIIS=lambda:map(int,I().split())

N = int(I())
solve([*MIIS()])

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
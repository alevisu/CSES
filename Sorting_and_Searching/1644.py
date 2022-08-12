from itertools import accumulate
from math import log2, ceil

class MaxTree:
	def __init__(self, arr) -> None:
		self.n = len(arr)
		self.d = [-INF]*N + arr + [-INF]*(N-len(arr))
		for i in range(N-1, 0, -1):
			self.d[i] = max(self.d[i<<1], self.d[i<<1|1]) 

	def max(self, s, e): # range [s; e] including e
		if e >= self.n: e = self.n - 1
		return self._max(1, 0, N-1, s, e)
	
	def _max(self, i, bs, be, s, e):
		if s>e: return -INF
		if bs==s and be==e: return self.d[i]
		bm = (bs+be) >> 1
		return max(	self._max(i<<1,   bs,   bm, s,            min(bm, e)),
								self._max(i<<1|1, bm+1, be, max(bm+1, s), e))
		
def solve(a, b, array):
	*psum, = accumulate(array)
	t = MaxTree(psum)
	m = -INF
	psum = [0]+psum
	# print(a, b, psum)
	for i in range(len(array)-a+1):
		m = max(m, t.max(i+a-1, i+b-1)-psum[i])
		# print(f"Testing {psum[i+a:i+b+1]}, i={i}, max={t.max(i+a-1, i+b-1)}, sub={psum[i]}, ans={m}")
	print(m)
	
LOCAL = False
if LOCAL:
	import sys
	from time import time
	start = time()

import io, os

INF = int(1.01e18)
I=io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
MIIS=lambda:[*map(int,I().split())]

N, A, B = MIIS()
N = 1 << ceil(log2(N))

solve(A, B, MIIS())

if LOCAL: print(f'Finished in {time()-start:.3f}sec',file=sys.stderr)
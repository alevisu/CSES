from math import log2, ceil

def solve(n, k):
	j = Josephus(n)
	rv, current = [], k%n
	for n in range(n-1, -1, -1):
		rv.append(str(j.kill(j.find_by_order(current))))
		if n: current = (current + k) % n
	print(' '.join(rv))


class Josephus: 
	def __init__(self, n):
		self.n = n
		self.size = 1 << ceil(log2(n)) # half size actually
		self.tree = [0]*self.size + [1]*n + [0]*(self.size-n) # Segment Tree
		for i in range(self.size-1, 0, -1):
			self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

	def __len__(self): return self.tree[1] # n of victims left in list
	def __repr__(self):	return f"{self.tree[1]}: {[n+1 for n, i in enumerate(self.tree[self.size:self.size+self.n]) if i>0]}"
	
	def kill(self, index):
		victim = index - self.size + 1
		self.tree[index] = 0
		while index > 1: 
			index >>= 1
			self.tree[index] -= 1
		return victim

	def find_by_order(self, target):
		remainder, index = target+1, 1
		while remainder != 0: # find node with exact sum
			if self.tree[index] > remainder: 
				index <<= 1
				continue
			remainder -= self.tree[index]
			if remainder > 0: index += 1
		while index < self.size: # find non-zero child with highest index
			index = index << 1 | 1
			if self.tree[index] == 0: index -= 1
		return index


I=input
MIIS=lambda:[*map(int,I().split())]

solve(*MIIS())
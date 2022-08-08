class Node:
	def __init__(self, data):
		self.d = data
		self.l = self.r = None
		self.h = 0
	def __repr__(self): return str(self.d)

class BST:
	def __init__(self, data=[]): 
		self.root = None
		self.size = len(data)
		self.sum = sum([x for x,_ in data])
		for d in data: self.root = self._add(self.root, d)

	def __len__(self): return self.size
	def __repr__(self): return 'BST{ ' + self.in_order(self.root) + '}'

	@staticmethod
	def height(node): 
		return -1 if node is None else node.h

	@staticmethod
	def balance(node):
		return 0 if node is None else BST.height(node.l) - BST.height(node.r)

	@staticmethod
	def get_min_value_node(node):
		if node is None or node.l is None:
			return node
		return BST.get_min_value_node(node.l)

	@property
	def min(self):
		node = self.root
		while node.l: node = node.l
		return node.d

	@property
	def max(self):
		node = self.root
		while node.r: node = node.r
		return node.d

	def remove(self, data):
		if self.root is None: return None
		self.root = self._remove(self.root, data)
		self.size -= 1
		self.sum -= data[0]
		return self

	# TODO: Write it!
	def _remove(self, node, data):
		if not node: return node
		if data < node.d:
			node.l = self._remove(node.l, data)
		elif data > node.d: 
			node.r = self._remove(node.r, data)
		else: # Node found
			if node.l is None: # no left subtree
				t = node.r
				node = None # clear parent's ref
				return t
			if node.r is None: # no right subtree
				t = node.l
				node = None # clear parent's ref
				return t
			# both subtrees are present
			t = BST.get_min_value_node(node.r) # get min from right
			node.d = t.d # update current root with its value
			node.r = self._remove(node.r, t.d) # and remove outdated node from right
		if not node: return node # in case we deleting max node
		
		node.h = 1 + max(BST.height(node.l), BST.height(node.r))
		node = BST.rebalance(node)

		return node


	def add(self, data):
		self.root = self._add(self.root, data)
		self.size += 1
		self.sum += data[0]
		return self

	def _add(self, node, data):
		if not node: return Node(data)
		if data < node.d: node.l = self._add(node.l, data)
		else: node.r = self._add(node.r, data)
		
		node.h = 1 + max(BST.height(node.l), BST.height(node.r))
		node = BST.rebalance(node)
		return node

	def find(self, data):
		return BST._find(self.root, data)

	@staticmethod
	def _find(node, data):
		if not node: return node
		if data < node.d: return BST._find(node.l, data)
		elif data > node.d: return BST._find(node.r, data)
		return node

	@staticmethod
	def rebalance(node):
		balance = BST.balance(node)
		if balance > 1:
			if BST.balance(node.l) >= 0:
				return BST.rotate_right(node)
			node.l = BST.rotate_left(node.l)
			return BST.rotate_right(node)
		if balance < -1:
			if BST.balance(node.r) <= 0:
				return BST.rotate_left(node)
			node.r = BST.rotate_right(node.r)
			return BST.rotate_left(node)
		return node

	@staticmethod
	def rotate_left(z):
		y = z.r; T2 = y.l
		y.l = z; z.r = T2
		z.h = 1 + max(BST.height(z.l), BST.height(z.r))
		y.h = 1 + max(BST.height(y.l), BST.height(y.r))
		return y

	@staticmethod
	def rotate_right(z):
		y = z.l; T3 = y.r
		y.r = z; z.l = T3
		z.h = 1 + max(BST.height(z.l), BST.height(z.r))
		y.h = 1 + max(BST.height(y.l), BST.height(y.r))
		return y

	def in_order(self, node):
		if not node: 
			if node is self.root: return "EMPTY "
			return ''
		rv = self.in_order(node.l)
		rv += str(node.d) + ' '
		return rv + self.in_order(node.r)
		
def solve(k, array):
	mid = (k // 2) + (k % 2)
	fw = sorted([(v, i) for i, v in enumerate(array[:k])])
	f, l = BST(fw[:mid]), BST(fw[mid:])
	
	# print(array)

	median = f.max[0]
	ans = [str(f.size*median-f.sum + l.sum-l.size*median)]
	for i, (rem, add) in enumerate(zip(array[:len(array)-k], array[k:]),k):
		# print(f"- Processing {i}: {rem, add}")
		
		if f.find((rem, i-k)): f.remove((rem, i-k))
		else: l.remove((rem, i-k))

		# we can just always add to first and move f.max to l afterwards
		# same results, but slower (too slow anyway tho)
		if f.size and add > f.max[0]: l.add((add, i))
		else: 
			f.add((add, i))
			if f.size == 1 and l.size and l.min < f.min:
				l, f = f, l

		if len(f) < mid:
			lmin = l.min
			f.add(lmin)
			l.remove(lmin)
		elif len(f) > mid:
			fmax = f.max
			f.remove(fmax)
			l.add(fmax)
		
		median = f.max[0]
		ans.append(str(f.size*median-f.sum + l.sum-l.size*median))

	
	print(' '.join(ans))

	



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

solve(MIIS()[1], MIIS())

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
from bisect import bisect

class TowersList:
	def __init__(self):
		self.towers = []

	def add(self, cube):
		tower_index = bisect(self.towers, cube)
		if tower_index == self.count:
			self.towers.append(cube)
			return
		self.towers[tower_index]=cube

	@property
	def count(self):
		return len(self.towers)

def solve():
	_ = I()
	towers = TowersList()
	for cube in MIIS(): towers.add(cube)
	print(towers.count)


# source of cringe, don't watch below this line!
import sys

LOCAL = False


try: 
	sys.stdin=open('ein.txt','r')
	# sys.stdout=open('out.txt', 'w')
	LOCAL = True
	def log(*a): print(*a,file=sys.stderr)
	from time import time
	start = time()
except FileNotFoundError:	
	pass

I=input
MIIS=lambda:[*map(int,I().split())]

solve()

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
class TrafficLight:
	def __init__(self, id, pos):
		self.id = id
		self.pos = pos
		self.prev = None
		self.next = None
	def pop(self):
		self.prev.next = self.next
		self.next.prev = self.prev
		return self.next.pos - self.prev.pos

def solve():
	x, n = MIIS()
	lights = MIIS()
	pos, longest = sorted(enumerate([0]+lights+[x]),key=lambda x: x[1]), 0
	for i in range(len(pos)-1):	longest = max(longest, pos[i+1][1]-pos[i][1])
	
	posmap = {}
	for id, p in pos: posmap[p] = TrafficLight(id, p)
	for i in range(1,len(pos)-1):
		posmap[pos[i][1]].prev = posmap[ pos[i-1][1] ]
		posmap[pos[i][1]].next = posmap[ pos[i+1][1] ]
	posmap[0].next = posmap[pos[1][1]]
	posmap[x].prev = posmap[pos[n+1][1]]

	result = [0]*n
	for i in range(len(lights)-1,-1,-1): 
		result[i] = longest
		longest = max(longest, posmap[lights[i]].pop())

	print(' '.join(str(x) for x in result))
	

# source of cringe, don't watch below this line!
import sys

LOCAL = False


try: 
	sys.stdin=open('in.txt','r')
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
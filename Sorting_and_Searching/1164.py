from heapq import heapify, heappush, heapreplace

def solve(customers):
	customers.sort()
	rooms, last_room, result = [[0, 1]], 1, [0] * N 
	heapify(rooms)
	for c in customers:
		room = rooms[0]
		if c[0] > room[0]: # room found 
			heapreplace(rooms, (c[1], room[1])) 
			result[c[2]] = str(room[1])
		else:
			last_room += 1
			heappush(rooms, (c[1], last_room))
			result[c[2]] = str(last_room)
	print(len(rooms))
	print(' '.join(result))
		




# source of cringe, don't watch below this line!
import sys

LOCAL = False


try: 
	sys.stdin=open('din.txt','r')
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
solve([(*MIIS(), id) for id in range(N)])

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
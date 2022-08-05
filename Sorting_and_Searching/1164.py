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
		
import sys

N = int(input())
solve([(int(a),int(b),int(id)) for id, (a, b) in zip(range(N),(l.split() for l in sys.stdin.readlines()))])


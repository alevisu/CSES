def solve(tasks):
	tasks.sort()
	points, time = 0, 0
	for t in tasks:
		time += t[0]
		points += t[1]-time
	print(points)



# source of cringe, don't watch below this line!
import sys

LOCAL = False


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

N = int(I())
solve([MIIS() for _ in range(N)])

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
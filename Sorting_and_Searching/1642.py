def solve(target, ints):
	sums = {}
	for i in range(0, N-1):
		for j in range(i+1, N):
			x = target - ints[i][1] - ints[j][1]
			if x in sums:	print(*[v+1 for v in (*sums[x], i, j)]); return
		for j in range(0, i): 
			sums[ints[i][1] + ints[j][1]] = (ints[i][0], ints[j][0])
	print('IMPOSSIBLE')
	# print(target, ints)


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
MIIS=lambda:map(int,I().split())

N, X = MIIS()
solve(X, [*enumerate(MIIS())])

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
def solve(target, array):
	a, b, s, n = 0, 0, array[0], 0
	try:
		while True:
			if s < target: b+=1; s+=array[b]
			elif s > target: s-=array[a]; a+=1 
			else: n += 1; b+=1; s+=array[b]
	except IndexError as e:
		LOCAL and log(e)
	print(n)


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
MIIS=lambda:[*map(int,I().split())]

N, X = MIIS()
solve(X, MIIS())

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
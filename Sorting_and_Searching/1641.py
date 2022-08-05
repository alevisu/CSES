def solve(target, ints):
	arr = sorted(ints, key=lambda x: x[1])
	for i in range(0, N-2):
		x, k = target - arr[i][1], N-1
		for j in range(i+1, N-1): 
			while arr[j][1]+arr[k][1]>x: k -= 1
			if j >= k: break
			if arr[j][1] + arr[k][1] == x:
				print(arr[i][0]+1, arr[j][0]+1, arr[k][0]+1)
				return
	print('IMPOSSIBLE')



# source of cringe, don't watch below this line!
import sys

LOCAL = False


try: 
	sys.stdin=open('in.txt','r') # ein - 3 1 4
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
from collections import defaultdict


def solve(k, array):
	answer, j = 0, 0
	dv = defaultdict(int)
	for i in range(len(array)): # slide a window
		while j < len(array): # until K distincts in it AND max window size
			if (len(dv) >= k) and (array[j] not in dv): break
			dv[array[j]] += 1
			j += 1
		answer += j-i # and window size will be the number of subarrays
		dv[array[i]] -= 1
		if dv[array[i]] == 0: del dv[array[i]]
	print(answer)


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

N, K = MIIS()
solve(K, MIIS())

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')
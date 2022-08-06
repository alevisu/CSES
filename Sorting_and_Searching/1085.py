def solve(k, array):
	lo = max(array)
	hi = ans = sum(array)
	while lo <= hi:
		mid, arr_sum, blocks = (lo+hi)//2, 0, 1
		b = []
		for i in array:
			if i+arr_sum>mid:
				blocks += 1
				arr_sum = 0
			arr_sum += i
		if blocks > k:
			lo = mid + 1
		else:
			ans = min(mid, ans)
			hi = mid - 1
	print(ans)




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
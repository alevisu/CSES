from bisect import bisect
try:import dotenv,sys;sys.stdin=open('in.txt','r')
except:pass

import time
start = time.time()

_=input()
prices=sorted(map(int,input().split()))

r=[]
for t in map(int,input().split()):
	i=bisect(prices, t)
	if i>0:	r.append(str(prices.pop(i-1)))
	else:	r.append("-1")
print("\n".join(r))

print(f"Finished in: {time.time()-start:.3f}sec", file=sys.stderr)
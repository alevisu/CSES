import sys

from time import time
start = time()
try:import dotenv;sys.stdin=open('in.txt','r')
except:pass
def log(*a):print(*a,file=sys.stderr)

input()
movies = {}
for a, b in (str.split(x) for x in sys.stdin.readlines()):
	ib = int(b)
	if ib not in movies: movies[ib]=int(a)
	else: movies[ib] = max(int(a), movies[ib])

cur, count = 0, 0
for m in sorted(movies.keys()):
	if movies[m] < cur: continue
	if cur <= m:
		count += 1
		cur = m

print(count)
log(f'Finished in {time()-start:.3f}sec')
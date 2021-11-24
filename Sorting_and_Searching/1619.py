import sys
from time import time
start = time()
try:import dotenv;sys.stdin=open('in.txt','r')
except:pass
def log(*a):print(*a,file=sys.stderr)
MIIS=lambda:map(int,input().split())

ab=[];input()
for x in map(str.split, sys.stdin.readlines()):
	ab+=[(int(x[0]),1),(int(x[1]),-1)]
def first(n): return n[0]
m=c=0;ab.sort(key=first)
for e in ab:
	c+=e[1]
	if c>m:m=c
print(m)

log(f'Finished in {time()-start:.3f}sec')

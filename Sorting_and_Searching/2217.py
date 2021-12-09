
from time import time
start = time()
import sys
try:import dotenv;sys.stdin=open('in.txt','r')
except:pass
def log(*a):print(*a,file=sys.stderr)
MIIS=lambda:map(int,input().split())

I=input;n,m=map(int,I().split());v=[-1]*(n+1)+[1<<24];s=l=0
x=[int(x) for x in I().split()]
swaps=[(a,b) for a,b in (map(int,l.split()) for l in sys.stdin.readlines())]
for i in range(n):v[x[i]]=i
for i in v:s+=i<l;l=i

print(x,s)
print(v)
for q,w in swaps[:5]:
	for i in [q,q+1,w,w+1]:
		# print(f"({v[i]}, {v[i-1]})")
		s-=v[i]<v[i-1]
	v[x[q-1]],v[x[w-1]]=v[x[w-1]],v[x[q-1]]
	for i in [q,q+1,w,w+1]:s+=v[i]<v[i-1]
	print(q,w,s)

log(f'Finished in {time()-start:.3f}sec')

"""
9 10 10 8 8
"""
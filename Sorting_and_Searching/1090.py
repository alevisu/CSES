from collections import deque
n,x=map(int,input().split())
p=deque(sorted(map(int,input().split())))

g=0
while p:
	g+=1; heavy=p.pop()
	if p and p[0]+heavy<=x: p.popleft()

print(g)
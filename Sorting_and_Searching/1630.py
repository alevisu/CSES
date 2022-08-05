import sys

I=input
N = int(I())
tasks = sorted([(int(d),int(f)) for d, f in (l.split() for l in sys.stdin.readlines())])
points, time = 0, 0
for t in tasks:
	time += t[0]
	points += t[1]-time
print(points)
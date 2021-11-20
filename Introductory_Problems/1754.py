nc=[]
for _ in range(int(input())): nc.append([*map(int, input().split())])
for p in nc:
	if sum(p)%3!=0 or sum(p)>min(p)*3:print("NO")
	else:print("YES")
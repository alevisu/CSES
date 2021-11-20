n=int(input())
if n==1 or n>3:
	print(*sum(([x for x in range(1,n+1) if x%2==y] for y in (0, 1)),[]))
else: print("NO SOLUTION")
for l in range(int(input())):
	y,x=map(int, input().split())
	n=max(x,y)
	a,b,x,y=(n-1)**2+1,n**2,x-1,y-1
	if n == x+1: r=b-y if x%2==0 else a+y
	else: r=b-x if y%2==1 else a+x
	print(r)
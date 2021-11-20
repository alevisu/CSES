n,m=input(),0
x=[0, *(int(a) for a in input().split())]
for i in range(1,len(x)):
	if x[i-1] > x[i]:	m, x[i] = m+x[i-1]-x[i], x[i-1]
print(m)


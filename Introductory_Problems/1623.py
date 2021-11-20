n=int(input())
p=list(sorted(map(int, input().split())))		 
res=set()
tm=p[n-1]*2
def net(i, s, path):
	if i==0: return res.add(abs(s))
	for m in [1,-1]: 
		t=m*p[i-1]
		if s+t<tm: net(i-1,s+t,path+[t])
net(n,0,[]);print(min(res))
p,n=print,int(input())
s=(1+n)*n//2
if s%2==1: p("NO");exit()
s//=2;p("YES")
a,b=set(range(1,n+1)),set()
for e in reversed(list(a)):
	if s==0:break
	if s<e:continue
	s-=e;b.add(e);a.remove(e)
p(len(a), "\n", *a)
p(len(b), "\n", *b)

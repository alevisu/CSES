I=input;n=int(I());v=[-1]*(n+1);s=l=0
x=[int(x) for x in I().split()]
for i in range(n):v[x[i]]=i
for i in v:s+=i<l;l=i
print(s)
n,s,m=int(input()),2,10**9+7
for i in range(n-1): s=(s<<1)%m
print(s)
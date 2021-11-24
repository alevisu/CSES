s=[-10**12]*int(input())
for i,v in enumerate(input().split()):s[i]=max(s[i-1]+int(v),int(v))
print(max(s))
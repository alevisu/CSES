input()
p=sorted(int(x) for x in input().split())
m=p[len(p)//2]
print(sum(abs(x-m) for x in p))
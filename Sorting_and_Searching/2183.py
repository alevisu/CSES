input();s=0
for c in sorted(int(v) for v in input().split()):
	if c-s>1:break
	s+=c
print(s+1)
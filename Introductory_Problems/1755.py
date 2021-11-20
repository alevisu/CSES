from collections import Counter
s,l=input(),Counter()
for c in s:	l[c]+=1
odd,even="",[]
for e, c in l.items():
	if c%2==1:
		if odd:print("NO SOLUTION");exit()
		odd=e
	else: even.append(e*(c//2))
print("".join([*even,odd*l[odd],*reversed(even)]))
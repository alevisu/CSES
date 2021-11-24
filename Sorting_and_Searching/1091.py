from bisect import bisect_left

_=input()
prices=sorted(map(int,input().split()))
cp = [prices[i:i+8] for i in range(0,len(prices),8)]
cpk = [x[0] for x in cp]

r=[]
for t in map(int,input().split()):
	chunk=bisect_left(cpk, t+1)-1
	if chunk>=0:
		i=bisect_left(cp[chunk], t+1)-1
		if i>=0:	
			r.append(str(cp[chunk].pop(i)))
			if i==0 and cp[chunk]: cpk[chunk]=cp[chunk][0]
			if not cp[chunk]: cp.pop(chunk); cpk.pop(chunk)
		else:	r.append("-1")
	else:	r.append("-1")
print("\n".join(r))
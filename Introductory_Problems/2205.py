n,c,l=int(input()),0,0
for i in range(1,2**n+1):
	t,msb=l^i,-1
	while t>0:t//=2;msb+=1
	print(bin(c)[2:].zfill(n))
	c^=(1<<msb);l=i
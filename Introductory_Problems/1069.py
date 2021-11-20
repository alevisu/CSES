s,l,m,o=input(),0,0,''
for c in s:
	if o!=c:l=0
	o,l,m=c,l+1,max(m,l+1)
print(m)
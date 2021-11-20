k=int(input())
def tk(k):
	n=28
	for k in range(1,k+1):
		if k<4:yield(0,6,28)[k-1];continue
		n+=(2*k-1)*(k-1)*k-16-(k-4)*8;yield n
print(*tk(k),sep="\n")
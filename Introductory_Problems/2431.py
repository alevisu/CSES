for k in range(int(input())):
	k, r = int(input()), 1
	while k > r*(9*10**(r-1)):	
		k, r = k-r*9*10**(r-1), r+1
	k-=1
	print(str((k//r)+10**(r-1))[k%r])
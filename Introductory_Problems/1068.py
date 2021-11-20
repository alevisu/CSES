def algo(n):
	while n != 1:
		yield n
		n = n//2 if n % 2 == 0 else n*3+1
		
print(*algo(int(input())),1)
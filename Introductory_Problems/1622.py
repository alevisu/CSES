string=input()
letters=list(string)
n,d=len(letters),len(set(letters))
variants,current=set(),[""]*n

def compose(current, letters):
	depth = n-len(letters)
	if depth==n: 
		variants.add("".join(current))
		return
	for i, letter in enumerate(letters):
		current[depth]=letter
		compose(current, [l for ii, l in enumerate(letters) if ii!=i])

compose(current, letters)
print(len(variants))
print(*sorted(variants),sep="\n")
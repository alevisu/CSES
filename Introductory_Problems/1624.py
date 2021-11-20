import sys
b=[l[:8] for l in sys.stdin.readlines()]
vars=set()
def q(p):
	n=len(p)
	if n==8: return vars.add(tuple(p))
	nq_row=n
	ep=list(enumerate(p))
	rd=tuple(range(-8,8))
	for nq_col in range(8):
		if (b[nq_row][nq_col]=="*") or nq_col in p: continue
		d=[(nq_row+i,nq_col+i) for i in rd]+[(nq_row+i,nq_col-i) for i in rd]
		d=[e for e in d if 0<=e[0]<=7 and 0<=e[1]<=7]
		if [q for q in d if q in ep]: continue
		q(p+[nq_col])

q([])
print(len(vars))
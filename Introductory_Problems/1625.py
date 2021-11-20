path=input()
d={'D':(0,1),'U':(0,-1),'L':(-1,0),'R':(1,0)}
n=[0,0]
def add(a,b): return (a[0]+b[0], a[1]+b[1])
def move(path, pos, grid):
	if len(path)==0:
		if pos==(0,6):n[0]+=1
		n[1]+=1; print(f"{n[0]} of {n[1]} (88418) [{n[1]/884.18:.02f}%]")
		return
	for step in [d[path[0]]] if path[0]!="?" else d.values(): 
		p=add(pos,step)
		if p in grid: continue
		g=grid.copy();g.add(p)
		move(path[1:],p,g)

frame=set((x,y) for x in range(-1,8) for y in range(-1,8) if x in [-1,7] or y in [-1,7])
move(path,(0,0),frame)
print(n)
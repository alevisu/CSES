i,pi,ri,s=input,0,0,0
n,m,k=map(int,i().split())
people=sorted(map(int, i().split()))
rooms=sorted(map(int, i().split()))+[-10]

while pi<len(people) and ri<len(rooms):
	if people[pi]+k<rooms[ri]: pi+=1; continue
	if people[pi]-k>rooms[ri]: ri+=1; continue
	s+=1;ri+=1;pi+=1

print(s)
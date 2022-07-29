#include <iostream>
#include <map>
#include <vector>

bool grid[81];
int step[48];
std::map<char, int> moves {{'D',9},{'L',-1},{'U',-9},{'R',1},{'?',0}};

int move(int i, int pos) {
	if(pos==64)return i==48?1:0;
	if(grid[pos-9]==grid[pos+9]&&grid[pos-1]==grid[pos+1])return 0;
	grid[pos]=1;
	int r=0; 
	if (step[i]) {if(!grid[pos+step[i]]) r+=move(i+1,pos+step[i]);}
	else {for (int step:{9,-1,-9,1}) {if(!grid[pos+step]) r+=move(i+1,pos+step);}}
	grid[pos]=0;
	return r;
}

int main() {
	std::cin.tie(0);
	std::string path; std::cin>>path;
	int it = 0;	for (char ch:path) {step[it++] = moves[ch];}
	for (int i=0;i<81;i++)if(i<=9||i>=72||i%9==0||i%9==8)grid[i]=1;
	std::cout<<move(0, 10)<<std::endl;
	return 0;
}

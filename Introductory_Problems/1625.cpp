#include <iostream>
#include <map>
#include <vector>

bool grid[81] {};
std::string path;
std::map<char, int> moves {{'D',9},{'L',-1},{'U',-9},{'R',1}};

int move(int pIndex, int pos) {
	if(pIndex==48||pos==64)return pIndex==48?1:0;
	if(grid[pos-9]==grid[pos+9]&&grid[pos-1]==grid[pos+1])return 0;
	grid[pos]=1;
	int r=0; std::vector<int> qmoves {9,-1,-9,1};
	if (path[pIndex]!='?') {qmoves = {moves[path[pIndex]]};}
	for (int step:qmoves){if(!grid[pos+step]) r+=move(pIndex+1,pos+step);}
	grid[pos]=0;
	return r;
}

int main() {
	std::cin>>path;
	for (int i=0;i<81;i++)if(i<=9||i>=72||i%9==0||i%9==8)grid[i]=1;
	std::cout<<move(0, 10)<<std::endl;
	return 0;
}
/*
##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
#K.Srinivasan
#NeuronRain Documentation and Licensing: https://neuronrain-documentation.readthedocs.io/en/latest/
#Personal website(research): https://acadpdrafts.readthedocs.io/en/latest/ 
#-----------------------------------------------------------------------------------------------------------
##############################################################################################################################################
*/

using namespace std;
#include <vector>
#include <iostream>
#include <cstdlib>

template<typename T>
class Point
{
	public:
		T x;
		T y;
};

class Lattice
{
	private:
		vector<Point<int>> walks;
	public:
		int latticewalkwithobstacles(vector<vector<int>>& lattice,int countwalks)
		{
			int rows = lattice.size();
			int columns = lattice[0].size();
			cout<<"Grid with obstacles"<<endl;
			if(countwalks)
			{
				vector<vector<int>> walks(rows, vector(columns,-1));
				findlatticewalks(0,0,rows,columns,lattice,walks);
				for (vector<vector<int>>::iterator it1=lattice.begin(); it1 != lattice.end(); it1++)
				{
					for(vector<int>::iterator it2=it1->begin(); it2 != it1->end(); it2++)
					{
						cout<<*it2<<",";
					}
					cout<<endl;
				}
				cout<<"Obstacle Free Lattice walks"<<endl;
				for(vector<vector<int>>::iterator it1=walks.begin(); it1 != walks.end(); it1++)
				{
					for(vector<int>::iterator it2=it1->begin(); it2 != it1->end(); it2++)
					{
						cout<<*it2<<",";
					}
					cout<<endl;
				}
			}
			else
			{
				findlatticewalks2(0,0,rows,columns,lattice);
				for (vector<vector<int>>::iterator it1=lattice.begin(); it1 != lattice.end(); it1++)
				{
					for(vector<int>::iterator it2=it1->begin(); it2 != it1->end(); it2++)
					{
						cout<<*it2<<",";
					}
					cout<<endl;
				}
				cout<<"Obstacle Free Lattice walks"<<endl;
				for (vector<Point<int>>::iterator it1=walks.begin(); it1 != walks.end(); it1++)
				{
					cout<<"("<<it1->x<<","<<it1->y<<")";
				}
			}
		}

		int findlatticewalks(int bottomx, int bottomy, int topx, int topy, vector<vector<int>>& lattice, vector<vector<int>>& walks)
		{
			if (bottomx == topx || bottomy == topy)
			{
				return 0;
			}
			if(bottomx == topx-1 && bottomy == topy-1)
			{
				return 1;
			}
			if (lattice[bottomx][bottomy] == 1)
			{
				return 0;
			}
			walks[bottomx][bottomy] = findlatticewalks(bottomx+1,bottomy,topx,topy,lattice,walks) + findlatticewalks(bottomx,bottomy+1,topx,topy,lattice,walks);
			return walks[bottomx][bottomy];
		}
		
		int findlatticewalks2(int bottomx, int bottomy, int topx, int topy, vector<vector<int>>& lattice)
		{
			if (bottomx == topx || bottomy == topy)
			{	
				Point<int> p;
				p.x = bottomx;
				p.y = bottomy;
				walks.push_back(p);
				return 0;
			}
			if(bottomx == topx-1 && bottomy == topy-1)
			{
				Point<int> p;
				p.x = bottomx;
				p.y = bottomy;
				walks.push_back(p);
				return 1;
			}
			if (lattice[bottomx][bottomy] == 1)
			{
				return 0;
			}
			findlatticewalks2(bottomx+1,bottomy,topx,topy,lattice);
			findlatticewalks2(bottomx,bottomy+1,topx,topy,lattice);
		}
};

int main()
{
	vector<vector<int>> grid = {{0,0,1,0,0,0},{0,1,0,0,0,1},{0,0,0,1,0,0},{0,1,0,1,0,0},{1,0,0,0,0,0},{1,0,0,0,0,0}};
	Lattice L;
	L.latticewalkwithobstacles(grid,1);
	L.latticewalkwithobstacles(grid,0);
}	


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>

using namespace std;
int productparity(unsigned long long a,unsigned long long b);

int main(int argc, char* argv[])
{
	vector<int> productparities;	
	char* end;
	unsigned long long x = strtoull(argv[1],&end,10);
	unsigned long long y = strtoull(argv[2],&end,10);
	for(unsigned long long i = 1; i <= x; i++)
	{
		for(unsigned long long j = 1; j <= y; j++)
		{
			int prod_par=productparity(i,j);
			productparities.push_back(prod_par);
		}
	}
	cout<<"======================================================"<<endl;
	cout<<"Produt Parity graph - plotted as Ferrer diagram"<<endl;
	cout<<"======================================================"<<endl;
	for(vector<int>::iterator it=productparities.begin();it != productparities.end();it++)
	{
		for(int i=1;i <= *it;i++)
		{
			cout<<"#";
		}
		cout<<endl;
	}
}

int productparity(unsigned long long a,unsigned long long b) 
{
	cout<<"==============================================="<<endl;
	cout<<"Product Parity of "<<a<<" * "<<b<<endl;
	cout<<"==============================================="<<endl;
	bitset<64> x(a);
	bitset<64> y(b);
	cout<<"binary x:"<<x<<" -- parity(number of 1s) -- "<<x.count()<<endl;
	cout<<"binary y:"<<y<<" -- parity(number of 1s) -- "<<y.count()<<endl;
	unsigned long long c=a*b;
	bitset<64> z(c);
	cout<<"binary x*y:"<<z<<" -- parity(number of 1s) -- "<<z.count()<<endl;
	return z.count();
}

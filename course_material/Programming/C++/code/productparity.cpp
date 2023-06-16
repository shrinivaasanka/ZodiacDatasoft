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
	char* end;
	productparity(strtoull(argv[1],&end,10),strtoull(argv[2],&end,10));
}

int productparity(unsigned long long a,unsigned long long b) 
{
	bitset<64> x(a);
	bitset<64> y(b);
	cout<<"binary x:"<<x<<" -- parity(number of 1s) -- "<<x.count()<<endl;
	cout<<"binary y:"<<y<<" -- parity(number of 1s) -- "<<y.count()<<endl;
	unsigned long long c=a*b;
	bitset<64> z(c);
	cout<<"binary x*y:"<<z<<" -- parity(number of 1s) -- "<<z.count()<<endl;
}

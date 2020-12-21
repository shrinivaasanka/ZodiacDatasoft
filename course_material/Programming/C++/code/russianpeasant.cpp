#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int russian_peasant_linear_multiplication(unsigned long long a,unsigned long long b);

int main(int argc, char* argv[])
{
	char* end;
	russian_peasant_linear_multiplication(strtoull(argv[1],&end,10),strtoull(argv[2],&end,10));
}

int russian_peasant_linear_multiplication(unsigned long long a,unsigned long long b) 
{
	unsigned long long tempa = a;
	unsigned long long tempb = b;
	unsigned long long product_ab = 0;
	while(true)
	{
		cout<<"tempa:"<<tempa<<endl;
		cout<<"tempb:"<<tempb<<endl;
		if(tempa % 2 == 1)
		{
			product_ab += tempb;
			if(tempa == 0 or tempa == 1)
				break;
		}
		tempa = tempa >> 1;
		tempb = tempb << 1;
	}
	cout<<"Product of "<<a<<" and "<<b<<":"<<product_ab<<endl;
}

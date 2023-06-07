#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int russian_peasant_linear_multiplication(unsigned long long a,unsigned long long b,double lowerboundepsilon);

int main(int argc, char* argv[])
{
	char* end;
	russian_peasant_linear_multiplication(strtoull(argv[1],&end,10),strtoull(argv[2],&end,10),strtod(argv[3],&end));
}

int russian_peasant_linear_multiplication(unsigned long long a,unsigned long long b,double lowerboundepsilon) 
{
	unsigned long long tempa = a;
	unsigned long long tempb = b;
	unsigned long long product_ab = 0;
	unsigned long long count = 0;
	cout<<"RUSSIAN PEASANT MULTIPLICATION"<<endl;
	cout<<"==================================="<<endl;
	while(true)
	{
		cout<<"tempa (factor1 / 2^"<<count<<"):"<<tempa<<" ------ tempb (factor2 * 2^"<<count<<"):"<<tempb<<endl;
		if(tempa % 2 == 1)
		{
			product_ab += tempb;
			if(tempa == 0 or tempa == 1)
				break;
		}
		tempa = tempa >> 1;
		tempb = tempb << 1;
		count += 1;
	}
	double lowerbound1 = (double) (std::log(a*b)/std::log(2)) - lowerboundepsilon;
	cout<<"Factor1 size(in bits):"<<std::log(a)/std::log(2)<<endl;
	cout<<"Factor2 size(in bits):"<<std::log(b)/std::log(2)<<endl;
	double lowerbound2 = (double) (std::log(a)/std::log(2) + std::log(b)/std::log(2) - lowerboundepsilon);
	cout<<"Approximate lower bound estimate 1 for last row,right column - 2^("<<lowerbound1<<"):"<<(unsigned long long) pow(2,lowerbound1)<<endl; 
	cout<<"Approximate lower bound estimate 2 for last row,right column - 2^("<<lowerbound2<<"):"<<(unsigned long long) pow(2,lowerbound2)<<endl; 
	cout<<"Product of "<<a<<" and "<<b<<":"<<product_ab<<endl;
}

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>

using namespace std;

extern "C"
{
#include "math.h"
}

int russian_peasant_linear_multiplication(unsigned long long a,unsigned long long b,double lowerboundepsilon);
unsigned long long computeLSB(int approx_parity,int leftshift);

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
		if(tempa % 2 == 1)
		{
			product_ab += tempb;
			cout<<"tempa (factor1 / 2^"<<count<<"):"<<tempa<<" ------ tempb (factor2 * 2^"<<count<<"):"<<tempb<<" ============= ODD Left Column ==================="<<endl;
			if(tempa == 0 or tempa == 1)
				break;
		}
		else
		{
			cout<<"tempa (factor1 / 2^"<<count<<"):"<<tempa<<" ------ tempb (factor2 * 2^"<<count<<"):"<<tempb<<endl;
		}
		tempa = tempa >> 1;
		tempb = tempb << 1;
		count += 1;
	}
	double lowerbound1 = (double) (std::log(a*b)/std::log(2)) - lowerboundepsilon;
	cout<<"Length of Russian peasant tableau:"<<count<<endl;
	cout<<"Factor1 size(in bits):"<<std::log(a)/std::log(2)<<endl;
	cout<<"Factor2 size(in bits):"<<std::log(b)/std::log(2)<<endl;
	double lowerbound2 = (double) (std::log(a)/std::log(2) + std::log(b)/std::log(2) - lowerboundepsilon);
	bitset<64> ab(product_ab);
	cout<<"ab.count():"<<ab.count()<<endl;
	int approx_parity = ab.count() >> 1 ;
	cout<<"Approximate Parity of left column (factor1) till penultimate row = ab.count()/2 :"<<approx_parity<<endl;
	int leftshift = count - approx_parity;
	cout<<"Leftshift(ab.count() - approximate_parity):"<<leftshift<<endl;
	unsigned long long leastsignificantbyte = computeLSB(approx_parity,leftshift);
	cout<<"Least significant byte:"<<leastsignificantbyte<<endl;
	unsigned long long lowerbound3 = (unsigned long long) (product_ab - leastsignificantbyte);
	cout<<"Lowerbound epsilon:"<<lowerboundepsilon<<endl;
	cout<<"Approximate lower bound estimate 1 for last row,right column - 2^("<<lowerbound1<<"):"<<(unsigned long long) pow(2,lowerbound1)<<endl; 
	cout<<"Approximate lower bound estimate 2 for last row,right column - 2^("<<lowerbound2<<"):"<<(unsigned long long) pow(2,lowerbound2)<<endl; 
	cout<<"Approximate estimate 3 for last row,right column :"<<lowerbound3<<endl; 
	cout<<"Product Factor1 * Factor2 of "<<a<<" and "<<b<<":"<<product_ab<<endl;
}

unsigned long long computeLSB(int approx_parity,int leftshift)
{
	unsigned long long lsb=0;
	for(int i=0;i < approx_parity;i++)
	{
		cout<<"computeLSB(): lsb = "<<lsb<<endl;
		lsb += pow(2,i); 
	}
	int leftshiftedlsb = lsb << leftshift;
	cout<<"leftshiftedlsb:"<<leftshiftedlsb<<endl;
	return leftshiftedlsb;
}

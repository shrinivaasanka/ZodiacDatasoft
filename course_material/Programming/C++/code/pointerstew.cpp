/*
##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
#K.Srinivasan
#NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
#Personal website(research): https://sites.google.com/site/kuja27/
#-----------------------------------------------------------------------------------------------------------
##############################################################################################################################################
*/

#include <iostream>

using namespace std;

class pointerstew
{
public:
	int x=1;
	int xx=x;
	//int&& rvaluerefx1=1;
	int&& rvaluerefx1=std::forward<int>(x);
	int& lvaluerefx2=x;
	void func1(int* p1, int* p2, int&& y)
	{
		cout<<"=================================="<<endl;
		cout<<"x="<<x<<endl;
		xx=std::move(y);
		cout<<"xx="<<xx<<endl;
		cout<<"pint1="<<*p1<<endl;
		cout<<"pint2="<<*p2<<endl;
		cout<<"rvaluerefx1="<<rvaluerefx1<<endl;
		cout<<"lvaluerefx2="<<lvaluerefx2<<endl;
		cout<<"=================================="<<endl;
	}

	void func1()
	{
		cout<<"=================================="<<endl;
		cout<<"x="<<x<<endl;
		cout<<"rvaluerefx1="<<rvaluerefx1<<endl;
		cout<<"lvaluerefx2="<<lvaluerefx2<<endl;
		cout<<"=================================="<<endl;
	}
};

int main()
{
	pointerstew* psptr;
	pointerstew ps;
	pointerstew& pslvalueref=ps;
	ps.rvaluerefx1++;
	int x=1;
	int *pint1=&x;
	int *pint2=&x;
	pslvalueref.func1();
	pint1=&ps.rvaluerefx1;
	pint2=&ps.lvaluerefx2;
	pslvalueref.func1(pint1,pint2,std::forward<int>(1));
	ps.lvaluerefx2++;
	pslvalueref.func1(pint1,pint2,std::forward<int>(1));
	psptr=&ps;
	psptr->x++;
	pslvalueref.func1(pint1,pint2,std::forward<int>(1));
}

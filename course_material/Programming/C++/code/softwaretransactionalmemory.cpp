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
#include <vector>
#include <thread>

using namespace std;

vector<int> globalvector;

int function1(int n)
{
	synchronized
	{
		int index=0;
		while(index++ < 10)
		{
			std::cout<<"function1(): globalvector.push_back() - "<<n<<endl;
			globalvector.push_back(n);
		}
	}
}

int function2() transaction_safe
{
	//Compiler errors:
	//g++-6 -g -fgnu-tm -o softwaretransactionalmemory softwaretransactionalmemory.cpp 
	//softwaretransactionalmemory.cpp:23:28: error: unsafe function call ‘void std::vector<_Tp, _Alloc>::push_back(std::vector<_Tp, _Alloc>::value_type&&) [with _Tp = int; _Alloc = std::allocator<int>]’ within ‘transaction_safe’ function
  	//globalvector.push_back(10);

	//g++-6 -g -fgnu-tm -o softwaretransactionalmemory softwaretransactionalmemory.cpp 
	//softwaretransactionalmemory.cpp:25:61: error: unsafe function call ‘std::basic_ostream<_CharT, _Traits>::__ostream_type& std::basic_ostream<_CharT, _Traits>::operator<<(std::basic_ostream<_CharT, _Traits>::__ostream_type& (*)(std::basic_ostream<_CharT, _Traits>::__ostream_type&)) [with _CharT = char; _Traits = std::char_traits<char>]’ within ‘transaction_safe’ function
  	//std::cout<<"function2(): globalvector.push_back() - "<<endl;
        //softwaretransactionalmemory.cpp:25:13: error: unsafe function call ‘std::basic_ostream<char, _Traits>& std::operator<<(std::basic_ostream<char, _Traits>&, const char*) [with _Traits = std::char_traits<char>]’ within ‘transaction_safe’ function
  	//std::cout<<"function2(): globalvector.push_back() - "<<endl;
        //     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	//std::cout<<"function2(): globalvector.push_back() - "<<endl;
	//globalvector.push_back(10);
}

int main()
{
	vector<thread> threads(10);
	for(auto& t: threads)
	{
		t=std::thread([]{for(int n=0; n < 10;n++) function1(n);});
	}
	for(auto& t: threads)
	{
		t.join();
	}
	for(auto& t: threads)
	{
		t=std::thread([]{for(int n=0; n < 10;n++) function2();});
	}
	for(auto& t: threads)
	{
		t.join();
	}
}

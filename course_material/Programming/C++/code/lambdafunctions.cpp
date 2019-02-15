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
#include <unordered_map>
#include <vector>
#include <functional>

using namespace std;

struct lambda
{
	std::unordered_map<string,int> hashmap;
	lambda()
	{	
		hashmap={{"one",1},{"two",2},{"three",3},{"four",4},{"five",5},{"six",6}};
	}

	std::function<int(string,int)> dynamicfunctions()
	{
		string seven="seven";
		int se7en=7;
		std::function<int(string,int)> function1=[this](string s,int n){this->hashmap[s]=n;return this->hashmap[s];};
		return function1;	
	}

	void printmap()
	{
		for(auto it:hashmap)
		{
			cout<<"it.first:"<<it.first<<endl;
			cout<<"it.second:"<<it.second<<endl;
		}
	}
};

int main()
{
	lambda lf;
	std::function<int(string,int)> function1=lf.dynamicfunctions();
	function1("seven",7);
	function1("eight",8);
	lf.printmap();
}

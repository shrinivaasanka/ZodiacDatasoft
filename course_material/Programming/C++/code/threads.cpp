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

using namespace std;

#include <string>
#include <unordered_map>
#include <thread>
#include <iostream>
#include <chrono>

unordered_map<std::string,int> hashmap;

int populate_hashmap(int i)
{
	std::this_thread::sleep_for(std::chrono::nanoseconds(i*i*i*i*i*i*i));
	cout<<"Move-assigned thread creation for value "<<i<<" ..."<<endl;
	hashmap.emplace(std::make_pair(std::to_string(i),i));
	if (i%2 == 0)
	{
		hashmap.max_load_factor(hashmap.max_load_factor()*3);
	}
	else
	{
		hashmap.rehash(3);
	}
}

int main()
{
	std::thread thr[50];
	for(int i=0; i < 50; i++) 
	{
		thr[i] = std::thread(populate_hashmap,i);
		thr[i].join();
	}
	for(auto it: hashmap)
	{
		cout<<"first="<<it.first<<"; second="<<it.second<<endl;
	}
}

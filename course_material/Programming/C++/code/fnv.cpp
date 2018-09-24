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

/*
Reference Example: https://www.boost.org/doc/libs/1_68_0/libs/unordered/examples/fnv1.hpp
Fowler-Noll-Vo - FNV - Hashing: http://www.isthe.com/chongo/tech/comp/fnv/
*/

using namespace std;

#include <string>
#include <iostream>
#include <unordered_map>

const size_t prime=37;
const size_t offset=232309321;

class fnvhash
{
public:
	template <size_t prime, size_t offset>
	struct fnv1a
	{
		size_t operator() (std::string s) const
		{
			size_t hash = offset;
			for(auto it: s)
			{
				hash ^= prime;
				hash *= it;
				//cout<<"hash:"<<hash<<endl;
			}
			cout<<"hash for ["<<s<<"]:"<<hash<<endl;
			return hash;
		}
	};
};


int main()
{
	fnvhash::fnv1a<prime,offset> fnv;
	fnv("string");
	unordered_map<std::string,std::string,fnvhash::fnv1a<prime,offset>> fnv_hashmap={{"java","3"},{"python","25"},{"chrome","43"},{"gcc","35"},{"ls","89"},{"ps -eaf","44"}};
	for(auto it: fnv_hashmap)
	{
		cout<<"first="<<it.first<<"; second="<<it.second<<endl;
	}
}

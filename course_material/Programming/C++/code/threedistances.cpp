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

int no_of_elements = 100;
int big=0,bigger=0,biggest=0;

class threedistances 
{
	float goldenratio = 0.618034;
public:
        size_t operator() (int n) const
        {
                        float goldfloat = n/goldenratio;
			int goldint = (int)goldfloat; 
			float hash = (goldfloat - goldint);
                        cout<<"hash for ["<<n<<"]:"<<hash<<endl;
			if(hash < 0.33)
			{
				cout<<"line segment is in big line segment set"<<";big="<<big<<endl;
				big++;
			}
			if(hash > 0.33 && hash < 0.66)	
			{
				cout<<"line segment is in bigger line segment set"<<";bigger="<<bigger<<endl;
				bigger++;
			}
			if(hash > 0.66)
			{
				cout<<"line segment is in biggest line segment set"<<";biggest="<<biggest<<endl;
				biggest++;
			}
			cout<<endl;
                        return (size_t)no_of_elements*hash;
        }
};

unordered_map<int,int,threedistances> hashmap;

int populate_hashmap(int n)
{
	hashmap.emplace(std::make_pair(n,n));
}

int main()
{
	for(int i=0; i < no_of_elements; i++) 
	{
		populate_hashmap(i);
	}
	for(auto it: hashmap)
	{
		cout<<"first="<<it.first<<"; second="<<it.second<<"; containing bucket = "<<hashmap.bucket(it.first)<<endl;
	}
}

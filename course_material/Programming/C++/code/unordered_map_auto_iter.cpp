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

#include <unordered_map>
#include <iostream>
#include <algorithm>

using namespace std;

int total=0;

void sum_duration(std::pair<string,int> val)
{
	total += val.second;
	cout<<"sum_duration(): total:"<<total<<endl;
}

int main()
{
	unordered_map<string,int> process_clocktick_map;
	process_clocktick_map={{"java",3},{"python",25},{"chrome",43},{"gcc",35},{"ls",89},{"ps -eaf",44}};
	for(auto it: process_clocktick_map)
	{
		cout<<"#################################"<<endl;
		cout<<"process:"<<it.first<<endl;
		cout<<"clockticks:"<<it.second<<endl;
		cout<<"bucket containing the process:"<<process_clocktick_map.bucket(it.first)<<endl;
	}	
	for_each(process_clocktick_map.begin(), process_clocktick_map.end(), sum_duration);
}

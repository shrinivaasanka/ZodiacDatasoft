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

#include <string>
#include <iostream>

using namespace std;
bool match_regex(int,std::string,std::string);
std::string globalregex="matchks";

int main()
{
	std::string s="dsdskjsjdksmatcsdkjkjmatchksldklmatch";
	match_regex(0,s,globalregex);
}

bool match_regex(int depth, std::string s, std::string regex)
{
	if(s != "" && regex != "")
	{
		if(s.at(0) == regex.at(0))
		{
			cout<<" :regexp "<<regex<<" matches at "<<depth<<endl;
			match_regex(depth+1,s.substr(1), regex.substr(1));
		}
		else
		{
			cout<<" :regexp "<<regex<<" does not match at "<<depth<<endl;
			match_regex(depth+1,s.substr(1),globalregex);
		}	
	}
}

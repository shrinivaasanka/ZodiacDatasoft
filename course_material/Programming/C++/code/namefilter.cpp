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
#include <fstream>
#include <sstream>
#include <vector>
#include <memory>
#include <iterator>
#include <algorithm>

using namespace std;

class namefilter
{
	std::string textfile;
	std::string text;
public:
	namefilter(const string& txtfile)
	{
		textfile=txtfile;
	}

	void filternames(string pattern)
	{
		ifstream txtfstr(textfile);
		int cnt=0;
		while(!txtfstr.eof())
		{
			std::shared_ptr<int> count=make_shared<int>(0);
			getline(txtfstr,text);
			stringstream sstr(text);
			istream_iterator<string> begin(sstr);
			istream_iterator<string> end;
			vector<string> vecstr(begin,end);
			//copy(vecstr.begin(),vecstr.end(),ostream_iterator<string>(cout,"\n"));
			copy(vecstr.begin(),vecstr.end(),vecstr.begin());
			std::vector<string> filtstr(vecstr.size());
			copy_if(vecstr.begin(),vecstr.end(),filtstr.begin(),[](string s){return (s.length() > 0);});
			for(auto it: filtstr)
			{
				if (it.find(pattern) != string::npos)
				{
					cnt++;
					std::shared_ptr<int> newcount=make_shared<int>(cnt);
					count.swap(newcount);
					cout<<"name filtered text:"<<it<<endl;
					cout<<"count shared_ptr:"<<*(count.get())<<endl;
				}
			}
		}
	}
};

int main()
{
	namefilter nfilt("namefilter.txt");
	nfilt.filternames("Sri");
}

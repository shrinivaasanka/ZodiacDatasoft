#include <iostream>
#include <string>
#include <random>
#include <algorithm> 

using namespace std;
void fisher_yates_knuth_shuffle(string s);

int main()
{
	string s="CDEFGAB";
	for(auto i=0; i <=10; i++)
	{
		cout<<"------- Shuffle "<<i<<"--------"<<endl;
		fisher_yates_knuth_shuffle(s);
	}
}

void fisher_yates_knuth_shuffle(string s)
{
	random_device dev;
	mt19937 rng(dev());
	int i=0;
	for(char &c: s)
	{
		int slen=s.length();
		cout<<"string length:"<<slen<<endl;
		if(i <= slen-2)
		{
			cout<<"random integer between "<<i<<" and "<<slen<<endl; 
			uniform_int_distribution<mt19937::result_type> dist(i,slen-1);
			int randindex = dist(rng);
			cout<<"random index:"<<randindex<<endl;
			cout<<"swap() "<<s[i]<<" and "<<s[randindex]<<endl;
			swap(s[i],s[randindex]);

		}
		i++;
	}
	cout<<"Fisher-Yates-Knuth shuffled string:"<<s<<endl;
}

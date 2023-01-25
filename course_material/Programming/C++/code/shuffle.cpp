#include <iostream>
#include <string>
#include <random>
#include <algorithm> 

using namespace std;
void fisher_yates_knuth_shuffle(string s);
void reservoir_sampling(string& s,string& r,int k);

int main()
{
	string s;
	string r;
	int k;
	cout<<"String to be shuffled (mostly a 12 notes octave sequence of CDEFGAB):"<<endl;
	cin>>s;
	cout<<"Length of string R:"<<endl;
	cin>>k;
	for(auto i=0; i <=10; i++)
	{
		cout<<"------- Shuffle "<<i<<"--------"<<endl;
		fisher_yates_knuth_shuffle(s);
		r.resize(k);
		reservoir_sampling(s,r,k);
	}
}

void reservoir_sampling(string& s,string& r,int k)
{
	random_device dev;
	mt19937 rng(dev());
	cout<<"-------------- Reservoir sampling -----------------"<<endl;
	cout<<"Before reservoir sampling - String S:"<<s<<endl;
	cout<<"Before reservoir sampling - String R:"<<r<<endl;
	for(auto i=0;i <= k;i++)
	{
		r[i] = s[i];
	}
	int slen=s.length();
	for(auto i=k+1;i < slen; i++)
	{
		uniform_int_distribution<mt19937::result_type> dist(1,i);
		int randindex = dist(rng);
		if(randindex < k)
		{
			cout<<"random index:"<<randindex<<endl;
			r[randindex]=s[i];
		}
	}
	cout<<"After reservoir sampling - String S:"<<s<<endl;
	cout<<"After reservoir sampling - String R:"<<r<<endl;
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

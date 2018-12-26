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
#include <string>
#include <unordered_map>

using namespace std;

class TimeoutImp
{
public:
	virtual void imptimeout()
	{
		cout<<"TimeoutImp::imptimeout()"<<endl;
	}
};

class Timeout
{
protected:
	TimeoutImp* timeoutimp;
public:
	virtual void timeout()
	{
		cout<<"Timeout::timeout()"<<endl;
	}
};

class TCPTimeout: public Timeout
{
public:
	TCPTimeout(TimeoutImp* toutimp)
	{
		timeoutimp=toutimp;
	}

	void timeout()
	{
		cout<<"TCPTimeout::timeout()"<<endl;
		timeoutimp->imptimeout();
	}
};

class TCPTimeoutImp: public TimeoutImp
{
	unordered_map<int,int> packets_timeouts;
public:
	TCPTimeoutImp()
	{
		packets_timeouts={{891299,12},{212121,21},{899899,34},{738278,67},{237878,55}};
	}

	void imptimeout()
	{
		cout<<"TCPTimeoutImp::imptimeout()"<<endl;
		for(auto it: packets_timeouts)
		{
			cout<<"===================================="<<endl;
			cout<<"TCP packet sequence number:"<<it.first<<endl;
			cout<<"Packet timeout TTL:"<<it.second<<endl;
			cout<<"===================================="<<endl;
		}
	}
};

int main()
{
	TCPTimeoutImp tcptimeoutimp;
	TimeoutImp* timeoutimp=&tcptimeoutimp;
	TCPTimeout tcptimeout(timeoutimp);
	tcptimeout.timeout();
}

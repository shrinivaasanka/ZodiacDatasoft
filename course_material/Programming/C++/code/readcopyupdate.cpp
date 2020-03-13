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
#include <thread>
#include <mutex>

using namespace std;
mutex mtx;

class readcopyupdate
{
	string value;
	string valuecopy;
	string copyalg="3";
public:
	readcopyupdate()
	{
	}

	readcopyupdate(string v):value(v)
	{
	}

	void setvalue(string v)
	{
		value=v;
	}

	string getvalue()
	{
		return value;
	}

	readcopyupdate& operator=(readcopyupdate& rvalue)
	{
		cout<<"operator= invoked"<<endl;
		//mtx.lock();
		//synchronized
		{
			cout<<"=================================="<<endl;
			cout<<"READ: lvalue="<<value<<endl;
			//Copy1 - Following does operator= invocation 
			if(copyalg=="1")
			{
				readcopyupdate lvaluecopy=*this;
				cout<<"COPY: lvaluecopy="<<lvaluecopy.value<<endl;
				lvaluecopy.value=rvalue.value;
				cout<<"UPDATE: lvaluecopy updated="<<lvaluecopy.value<<endl;
				value=lvaluecopy.value;
			}
			//Copy2 - Following two lines iteratively assign 
			if(copyalg=="2")
			{
				readcopyupdate lvaluecopy;
				cout<<"COPY: lvaluecopy="<<lvaluecopy.value<<endl;
				lvaluecopy.value=rvalue.value;
				cout<<"UPDATE: lvaluecopy updated="<<lvaluecopy.value<<endl;
				value=lvaluecopy.value;
			}
			//Copy3 - private variable valuecopy is assigned
			if(copyalg=="3")
			{
				valuecopy=value;
				cout<<"COPY: valuecopy="<<valuecopy<<endl;
				valuecopy=rvalue.value;
				cout<<"UPDATE: lvaluecopy updated="<<valuecopy<<endl;
				value=valuecopy;
			}
			cout<<"WRITEBACK: lvalue updated="<<value<<endl;
			cout<<"=================================="<<endl;
		}
		//mtx.unlock();
	}
};

readcopyupdate lvalue;

int multithreaded_read(int i)
{
	cout<<"multithreaded_read(): thread-"<<to_string(i)<<" lvalue="<<lvalue.getvalue()<<endl;
}

int multithreaded_rcu_assign(int i)
{
	string rv="rvalue";
	readcopyupdate rvalue(rv.append(to_string(i)));
	cout<<"multithreaded_rcu_assign(): thread-"<<to_string(i)<<endl;
	lvalue=rvalue;
}

int main()
{
	lvalue.setvalue("lvalue");
	std::thread thr1[100];
	std::thread thr2[100];
	for(int i=0; i < 100; i++)
	{
        	thr1[i] = std::thread(multithreaded_rcu_assign,i);
                thr1[i].join();
        	thr2[i] = std::thread(multithreaded_read,i);
                thr2[i].join();
	}
}

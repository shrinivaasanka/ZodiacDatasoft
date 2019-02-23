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

#include <vector>
#include <thread>
#include <future>
#include <iostream>

using namespace std;

chrono::time_point<chrono::high_resolution_clock> epoch;

int train(promise<double> signal_promise, string name)
{
	//While loop causes runtime error:
	//terminate called after throwing an instance of 'std::future_error'
  	//what():  std::future_error: Promise already satisfied

	//while(true)
	//{
		cout<<"Train "<<name<<endl;
		auto time=chrono::high_resolution_clock::now();
		std::chrono::duration<double> dur=time-epoch;
		signal_promise.set_value(dur.count());	
	//}
}

int main()
{
	promise<double> signal_promise1;
	promise<double> signal_promise2;
	future<double> signal_future1=signal_promise1.get_future();
	future<double> signal_future2=signal_promise2.get_future();
	thread train1(train,move(signal_promise1),"train1");
	thread train2(train,move(signal_promise2),"train2");
	signal_future1.wait();
	signal_future2.wait();
	cout<<"Signal Future 1"<<signal_future1.get()<<endl;
	cout<<"Signal Future 2"<<signal_future2.get()<<endl;
	train1.join();
	train2.join();
}

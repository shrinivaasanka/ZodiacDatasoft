#include <iostream>
#include <string>
#include <typeinfo>
#include <algorithm>

using namespace std;

template<typename T>
class This 
{
	T str;
public:
	This()
	{
		cout<<"this..."<<this<<endl;
		cout<<"overwriting this..."<<endl;
		This*&& rvaluethis=this; 
		cout<<"rvaluethis :"<<rvaluethis<<endl;
		/*
		//Old-style this override - vide page 631 - Reference manual - The C++ Programming Language - Bjarne Stroustrup
		//present compiler standards prefer operator new
		this = rvaluethis;
		*/
	}

	This(T str1)
	{
		str=str1;
	}

	void* operator new(size_t size)
	{
		cout<<"operator new overloaded and this is from a heap allocator"<<endl;
		void* allocator=malloc(size*sizeof(This));	
		return (void*)allocator;
	}

	void* operator new(size_t size, void* placementstorage)
	{
		return (void*) placementstorage;
	}

	~This()
	{
		/*
		//Old-style this override - vide page 631 - Reference manual - The C++ Programming Language - Bjarne Stroustrup
		//present compiler standards prefer operator delete 
		this=0;
		*/
	}

	void operator delete(void* p)
	{
		cout<<"operator delete overloaded and this is freed to a heap allocator"<<endl;
		free((void*)p);
	}	
};

main()
{
	cout<<"====================================="<<endl;
	cout<<"auto allocation"<<endl;
	cout<<"====================================="<<endl;
	This<string> s1;
	cout<<"====================================="<<endl;
	cout<<"operator new:"<<endl;
	cout<<"====================================="<<endl;
	This<string>* s2=new This<string>();
	delete s2;
	char allocator[500];
	cout<<"====================================="<<endl;
	cout<<"placement operator new:"<<endl;
	cout<<"====================================="<<endl;
	This<string>* s3=new (allocator) This<string>();
}

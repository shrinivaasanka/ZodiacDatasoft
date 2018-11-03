#include <iostream>
#include <typeinfo>
#include <string>
#include <cxxabi.h>

using namespace std;

class Animal 
{
	int number_of_legs;
protected:
	int number_of_wings;
public:
	Animal()
	{
		cout<<"base class Animal"<<endl;
	}
	virtual void trait()=0;
	const virtual int legs() const 
	{
		cout<<"const number_of_legs"<<endl;
		cout<<"number of legs "<<number_of_legs<<endl;
		return number_of_legs;
	}
	const virtual int legs() 
	{
	}
	friend class Lion;
	friend class Tiger;
};

class Lion: public Animal 
{
	bool mammal;
public:
	Lion(bool m, int l,int w):mammal(m)
	{
		Animal::number_of_legs = l;
		Animal::number_of_wings = w;
	}

	const int legs()
	{
		trait();
		cout<<"adding 4 more legs"<<endl;
		number_of_legs+=4;
		cout<<"number of legs "<<number_of_legs<<endl;
		return number_of_legs;
	}

	int wings() const
	{
		cout<<"number of wings "<<number_of_wings<<endl;
		return number_of_wings;
	}

	void trait()
	{
		int status;
		cout<<abi::__cxa_demangle(typeid(this).name(),NULL,NULL,&status)<<" roars"<<endl;
	}
};

class Tiger: public Animal
{
	bool mammal;
public:
	Tiger(bool m,int l,int w):mammal(m)
	{
		Animal::number_of_legs = l;
		Animal::number_of_wings = w;
	}

	const int legs()
	{
		trait();
		cout<<"adding 4 more legs"<<endl;
		number_of_legs+=4;
		cout<<"number of legs "<<number_of_legs<<endl;
		return number_of_legs;
	}

	int wings() const
	{
		cout<<"number of wings "<<number_of_wings<<endl;
		return number_of_wings;
	}

	void trait()
	{
		int status;
		cout<<abi::__cxa_demangle(typeid(this).name(),NULL,NULL,&status)<<" gallops"<<endl;
	}
};

int main()
{
	Lion l(true,4,0);
	l.trait();
	l.wings(); 
	cout<<"========================="<<endl;
	Tiger t(true,4,0);
	t.trait();
	t.wings();
	cout<<"========================="<<endl;
	const Animal *a=&l;
	const Animal *b=&t;
	a->legs();
	b->legs();
	cout<<"========================="<<endl;
	l.legs();
	t.legs();
}

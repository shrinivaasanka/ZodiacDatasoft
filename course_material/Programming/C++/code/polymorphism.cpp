#include <iostream>
#include <typeinfo>
#include <string>

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
	virtual int legs() const 
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

	int legs() const
	{
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
		cout<<typeid(this).name()<<" roars"<<endl;
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

	int legs() const
	{
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
		cout<<typeid(this).name()<<" gallops"<<endl;
	}
};

int main()
{
	Lion l(true,4,0);
	l.trait();
	l.legs();
	l.wings(); 
	cout<<"========================="<<endl;
	Tiger t(true,4,0);
	t.trait();
	t.legs();
	t.wings();
}

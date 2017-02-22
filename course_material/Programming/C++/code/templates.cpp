#include <iostream>
#include <string>
#include <typeinfo>

using namespace std;

template<typename T>
class Book
{
	int num_of_pages;
	string title;
	T booktype;
public:
	Book()
	{
	}

	Book(T type)
	{
		booktype=type;
		cout<<"Instantiating Book of type "<<booktype<<endl;
		cout<<"template type:"<<typeid(booktype).name()<<endl;
	}

	virtual void read_book()
	{
		cout<<"Read book"<<endl;
	}
};

template<typename T>
class EBook: public Book<T>
{
public:
	EBook(T type)
	{
		cout<<"Instantiating EBook of type "<<type<<endl;
	}
};

int main()
{
	Book<string> b1("Maths");
	Book<string> b2("ComputerScience");
	Book<string> b3("Physics");
	Book<string> b4("History");
	EBook<string> b5("English");
	b1.read_book();
	b2.read_book();
	b3.read_book();
	b4.read_book();
	b5.read_book();
}

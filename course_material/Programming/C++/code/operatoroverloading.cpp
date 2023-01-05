#include <iostream>

using namespace std;

class String
{
	std::string s;
public:
	String(std::string txt)
	{
		s=txt;
		cout<<"String(): s="<<txt<<endl;
	}
	String& operator<=>(String& s1) 
	{
		std::strong_ordering ret = (s.c_str() <=> s1.s.c_str());
		if (ret > 0)
			cout<<"operator<=>():ret > 0"<<endl;
		if (ret == 0)
			cout<<"operator<=>():ret = 0"<<endl;
		if (ret < 0)
			cout<<"operator<=>():ret < 0"<<endl;
		return *this;
	}
	String& operator+=(String& s1)
	{
		s=this->s+s1.s;
		cout<<"operator+=(): s="<<s<<endl;
		return *this;
	}
};

int main()
{
	String string1("string1");
	String string2("string2");
	String ret=string1<=>string2;
	string1+=string2;
}

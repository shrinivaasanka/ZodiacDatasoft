#include <iostream>
#include <string>
#include <typeinfo>
#include <algorithm>

using namespace std;

template<typename T>
class UniqueString 
{
	T str;
public:
	UniqueString()
	{
	}

	UniqueString(T str1)
	{
		str=str1;
	}

	bool duplicateexists()
	{
		for(int n=0; n < str.length(); n++)
		{
			if (n > 0 && str[n] == str[n-1])
			{
				cout<<"duplicateexists(): true"<<endl;
				return true;
			}
		}
		return false;
	}

	void remove_duplicates()
	{
		sort(str.begin(),str.end());
		int present = 0;
		while (present < str.length() || duplicateexists())
		{
			cout<<"str:"<<str<<endl;
			if (present > 0)
			{
				if(str[present-1] == str[present])
				{
					str.erase(present,1);
				}
			}
			present += 1;
			if (present > str.length())
				present = 0;
		}		
		cout<<"remove_duplicates(): unique string = "<<str<<endl;
	}
};

main()
{
	UniqueString<string> s("aaadsjdggdds9jsdkbbbcccdddeeeff");
	s.remove_duplicates(); 
}

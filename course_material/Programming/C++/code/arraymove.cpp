#include <stdio.h>
#include <string.h>
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>

using namespace std;

int reference_array_move(reference_wrapper<string> (&array2)[8]);
int main()
{
	int cnt=0;
	int array[] = {1,2,3,4,5,6,7,8};
	vector<int> arrayv(array,array+8);
	rotate(arrayv.begin(), arrayv.begin()+3,arrayv.end());
	int *arrayvdata=arrayv.data();
	int arraylength=arrayv.size();
	for(int n=0;n<arraylength;n++)
	{
		cout<<"rotated array element["<<n<<"]:"<<arrayvdata[n]<<endl;
		cnt++;
	}
	cnt=0;
	string stringone("string1");
	string stringtwo("string2");
	string stringthree("string3");
	string stringfour("string4");
	string stringfive("string5");
	string stringsix("string6");
	string stringseven("string7");
	string stringeight("string8");
	reference_wrapper<string> array2[] = {stringone,stringtwo,stringthree,stringfour,stringfive,stringsix,stringseven,stringeight};
	memmove(array,array+3,sizeof(array));
	for(auto& elem: array)
	{
		cout<<"moved array element["<<cnt<<"]:"<<array[cnt]<<endl;
		cnt++;
	}
	reference_array_move(array2);
}

int reference_array_move(reference_wrapper<string> (&array2)[8])
{
	memmove(array2,array2+3,sizeof(array2));
	int cnt=0;
	for(auto& elem: array2)
	{
		cout<<"moved array2 element["<<cnt<<"]:"<<array2[cnt].get()<<endl;
		cnt++;
	}
}

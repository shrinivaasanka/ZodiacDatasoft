#include <algorithm>
#include <iostream>
#include <array>

using namespace std;
template <typename Type,std::size_t... dynsize>
auto dynamic_std_array(const std::array<Type,dynsize>&... arrays)
{
	std::array<Type, (dynsize + ...)> dynarray;
	std::size_t index{};
	cout<<"dynamic_std_array() fold expression .... "<<endl;
	((std::copy_n(arrays.begin(),dynsize,dynarray.begin() + index),index += dynsize), ...);
	return dynarray;
}

int main(int argc, char* argv[])
{
	const int dynsize = std::atoi(argv[1]);
	cout<<"1.Allocating array on stack of size:"<<dynsize<<endl;
	int dynarray1[dynsize];
	dynarray1[0]=1;
	cout<<"dynarray1[0]="<<dynarray1[0]<<endl;
	cout<<"2.Allocating array on heap of size:"<<dynsize<<endl;
	int *dynarray2;
        dynarray2 = new int[dynsize];	
	dynarray2[0]=1;
	cout<<"dynarray2[0]="<<dynarray2[0]<<endl;
	cout<<"3.Allocating std::array of type int and size "<<dynsize<<endl;
	const std::array<int,10> dynarray3{};
	const std::array<int,10> dynarray4{};
	const std::array<int,10> dynarray5{};
	const auto dynarray6=dynamic_std_array(dynarray3,dynarray4,dynarray5);
	cout<<"dynarray6[0]="<<dynarray6[0]<<endl;
	cout<<"number of elements in dynarray6="<<dynarray6.size()<<endl;
}


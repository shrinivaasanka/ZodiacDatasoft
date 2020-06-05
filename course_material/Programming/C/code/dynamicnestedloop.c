#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void nestedloop(int from,int to,int depth, int (*loopbody)(int,int*),int* counter);
int loopbody(int depth,int* counter);

int main()
{
	int count=0;
	nestedloop(0,10,3,loopbody,&count);
}

void nestedloop(int from,int to,int depth, int (*loopbody)(int,int*),int* counter)
{
	if(depth == 0)
		return;
	for(int i=from;i < to;i++)
	{
		nestedloop(from,to,depth-1,loopbody,counter);
		loopbody(depth,counter);
	}
}

int loopbody(int depth,int* counter)
{
	if(depth == 1)
		printf("nested for loop - depth %d - count %d \n",depth,++(*counter));
}

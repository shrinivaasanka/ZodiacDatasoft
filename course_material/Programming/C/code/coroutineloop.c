#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void loop(int* count,int* variable);
void loop2(int* count,int* variable);

int main(int argc,char* argv[])
{
	int count=atoi(argv[1]);
	int variable=atoi(argv[2]);
	loop(&count,&variable);
	printf("count decremented after coroutine looping : %d\n",count);
	printf("variable incremented after coroutine looping : %d\n",variable);
}

void loop(int* count,int* variable)
{
	printf("loop(): *count = %d \n",*count);
	printf("loop(): *variable = %d \n",*variable);
	if (*count==0)
	{
		printf("loop(): returning *variable = %d \n",*variable);
		return;
	}
	(*variable)++;
	(*count)--;
	loop2(count,variable);
}

void loop2(int* count,int* variable)
{
	printf("loop2(): count = %d \n",*count);
	printf("loop2(): *variable = %d \n",*variable);
	if (*count==0)
	{
		printf("loop2(): returning *variable = %d \n",*variable);
		return;
	}
	(*variable)++;
	(*count)--;
	loop(count,variable);
}

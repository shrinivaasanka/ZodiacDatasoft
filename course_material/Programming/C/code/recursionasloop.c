#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void loop(void* x,int start,int end,int arg);
int main()
{
	int searchtree1[]={0,1,2,5,7,15,16,27,38,9999};
	int searchtree2[]={0,11,2,5,7,15,166,27,38,9999};
	int n=0;
	int count=10;
	loop(&n,count,0,1);
	printf("n=%d\n",n);
	printf("Search Tree 1:\n");
	loop(searchtree1,0,9,2);
	printf("Search Tree 2:\n");
	loop(searchtree2,0,9,2);
}

void loop(void* obj,int start,int end,int arg)
{
	if(arg == 1)
	{		
			int* x1 = (int*)obj;
			if(*x1 == start)
			{
	    			printf("*x1=%d\n",*x1);
	    			return;
			}
			else
			{
	    			printf("*x1=%d\n",*x1);
	    			(*x1)++;
	    			loop(x1,start,0,1);
			}
	}
	else
	{
			int* x2 = (int*)obj;
			int cnt=end-start;
			if(cnt == 1)
			{
				return;
			}
			else
			{
				if(x2[start] < x2[start+cnt/2])
				{
					printf("comparison: %d %d \n",x2[start],x2[start+cnt/2]);
					loop(x2,start,start+cnt/2,2);
				}
				else
					printf("array is not inorder traversal of binary search tree\n");
				if(x2[start+cnt/2] < x2[end])
				{
					printf("comparison: %d %d \n",x2[start+cnt/2],x2[end]);
					loop(x2,start+cnt/2,end,2);
				}
				else
					printf("array is not inorder traversal of binary search tree\n");
			}
	};
}

#include <stdio.h>

int tob (int b, int* arr);
int pp(int a, int b);

int main()
{
	int a[4][5]={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20}};
	int ret=1;
	printf("**a = %d\n",**a);
	printf("**(a + **a + 2) = %d\n",**(a + **a + 2));
	printf("*(*(a + **a + 2) + 3) = %d\n",*(*(a + **a + 2) + 3));
	ret=pp(3,4);
	printf("pp(3,4) = %d\n",ret);
	ret=pp(3,5);
	printf("pp(3,5) = %d\n",ret);
	ret=pp(3,6);
	printf("pp(3,6) = %d\n",ret);
	ret=pp(3,7);
	printf("pp(3,7) = %d\n",ret);
}

int tob (int b, int* arr) 
{
    int i;
    for (i = 0; b>0; i++)  
    {
        if (b%2)  
		arr[i] = 1;
        else    
		arr[i] = 0;
        b = b/2;
    }
    return (i);
}

int pp(int a, int b)  
{
    int  arr[20];
    int i, tot = 1, ex, len;
    ex = a;
    len = tob(b, arr);
    for (i=0; i<len ; i++) 
    {
	 printf("array[%d] - %d \n",i,arr[i]);
         if (arr[i] == 1)
             tot = tot * ex;
         ex= ex*ex;
    }
    return (tot) ;
}

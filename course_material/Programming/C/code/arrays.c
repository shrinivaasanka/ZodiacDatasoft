#include <stdio.h>

int main()
{
	static int a[3];
	a[0]=7;
	a[1]=8;
	a[2]=9;
	printf("a[2] : %d\n",a[2]);
	printf("2[a] + a[2] : %d\n",2[a] + a[2]);
	printf("a[2] = 2[a] : %d\n",a[2] = 2[a]);
	printf("a[2] = 2[a] + a[2] : %d\n",a[2] = 2[a] + a[2]);
	printf("a[2] : %d \n",a[2]);
	printf("a[2] == 2[a] + a[2] : %d\n",a[2] == 2[a] + a[2]);
	printf("a[2] : %d \n",a[2]);
	printf("(a[2] == 2[a]) + a[2] : %d\n",(a[2] == 2[a]) + a[2]);
	printf("a[2] : %d \n",a[2]);
}

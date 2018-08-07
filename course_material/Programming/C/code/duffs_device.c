#include <stdio.h>

int main()
{
	int n=30;
	do
	{
		switch(n%5)
		{
		case 0:
			n--;
			printf("0: %d \n",n);
		case 1:
			n--;
			printf("1: %d \n",n);
		case 2:
			n--;
			printf("2: %d \n",n);
		case 3:
			n--;
			printf("3: %d \n",n);
		case 4:
			n--;
			printf("4: %d \n",n);
		};
	}
	while(n > 0);
}	

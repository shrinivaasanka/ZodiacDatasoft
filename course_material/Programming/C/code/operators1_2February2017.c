/*
	Code example from C Puzzle Book - Alan R.Feuer - Page 5
*/

#include <stdio.h>

main()
{
	int x;
	x = -3 + 4 * 5 - 6; printf("%d\n",x);
	x = 3 + 4 % 5 - 6; printf("%d\n",x);
	x = -3 * 4 % -6 / 5; printf("%d\n",x);
	x = (7 + 6) % 5 / 2; printf("%d\n",x);
}

/*
	Above prints:
	11
	1
	0
	1
*/

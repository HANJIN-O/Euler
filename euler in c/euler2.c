#include <stdio.h>

int main()
{
	int sum = 2;
	int x = 3;
	int x1 = 2;
	int x2 = 1; //x는 현재항 x1은 바로앞항 x2는 두개앞항
	while(x <= 4000000)
	{
		if (x%2==0)
		{
		sum += x;
		}
		printf ("%d \n", x);
		x = x1 + x2;
		x2 = x1;
		x1 = x;
	}
	
	printf("sum = %d", sum);
	return 0;
}

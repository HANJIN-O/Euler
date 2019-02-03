#include <stdio.h>
#define BOOL int
#define TRUE 1
#define FALSE 0


int main()
{
		unsigned long result = 2;
		for(int j=3; j<2000001; j++)
		{
				if(pfactor(j))
				{
						printf("%d is prime factor\n", j);
						result += j;
						printf("sum = %d \n", result);
				}
		}

		return 0;
}

BOOL pfactor(unsigned int num)
{
		for (unsigned i=2; i<num; i++)
		{
				if (num%i==0)
						return FALSE;
		}
		return TRUE;
}

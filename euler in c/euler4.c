#include <stdio.h>

int main()
{
		int num1;
		int num2;
		int value;
		int array1[5]={0};
		int array2[6]={0};
		int answer=0;

		for(num1=100; num1<1000; num1++)
		{
				for(num2=100; num2<1000; num2++)
				{
						value=num1*num2;

						//cut into digit and put it into array
						if(value<100000)
						{
								array1[4]=value % 10;
								array1[3]=value / 10 % 10;
								array1[2]=value / 100 % 10;
								array1[1]=value / 1000 % 10;
								array1[0]=value / 10000 % 10;


								if(array1[0]==array1[4]&&array1[1]==array1[3])
								{
										if(value>answer)
										{
												answer=value;
										}
								}


						}
						else
						{
								array2[5]=value % 10;
								array2[4]=value / 10 % 10;
								array2[3]=value / 100 % 10;
								array2[2]=value / 1000 % 10;
								array2[1]=value / 10000 % 10;
								array2[0]=value / 100000 % 10;

								if(array2[0]==array2[5]&&array2[1]==array2[4]&&array2[2]==array2[3])
								{
										if(value>answer)
										{
												answer=value;
										}
								}

						}

						/*
						//find length of array
						int size=sizeof(array_test)/sizeof(array_test[0]);
		
						for(int i=0; i<size; i++)
						{
						printf("%d", array_test[i]);
						}
						*/
				}
		}
		printf("%d is the biggest palindrome! \n", answer);

		return 0;
}

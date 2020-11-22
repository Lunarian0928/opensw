#include <stdio.h>

void func1(int* p); // pointer + 100
void func2(int** p); // double pointer + 100
void func3(int*** p); // triple pointer + 100
void func4(int**** p); // quadra pointer + 100

int main() {
	int i = 100;

	int *p, **dp, ***tp;

	p = &i; // pointer of i
	dp = &p; // double pointer of i
	tp = &dp; // triple pointer of i

	func1(&i);
	printf("i = %d\n", i);

	func2(&p);
	printf("*p = %d\n", *p);

	func3(&dp);
	printf("**dp = %d\n", **dp);

	func4(&tp);
	printf("***tp = %d\n", ***tp);

	printf("i = %d\n", i);

	return 0;

}

void func1(int* p)
{
	*p = *p+100;
}

void func2(int** p)
{
	**p = **p+100;
}

void func3(int*** p)
{
	***p = ***p+100;
}

void func4(int**** p)
{
	****p = ****p+100;
}

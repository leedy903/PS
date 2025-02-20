#include <stdio.h>
int factorial(int n);
int main(void) {
	int N = 0;
	scanf("%d", &N);
	printf("%d", factorial(N));
	return 0;
}
int factorial(int n) {
	if (n) return factorial(n - 1)*n;
	else return 1;
}
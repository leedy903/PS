#include <stdio.h>
int main(void) {
	int A, B = 0;
	scanf("%d %d", &A, &B);
	printf("%d\n%d\n%d\n%d\n", B%10*A, B/10%10*A, B/100%10*A, B*A);
	return 0;
}
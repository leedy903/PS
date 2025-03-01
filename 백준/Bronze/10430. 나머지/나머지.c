#include <stdio.h>

int main(void) {
	int A = 1, B = 1, C = 1;
	while (A < 2 || B < 2 || C < 2 || A > 10000 || B > 10000 || C > 10000) {
		scanf("%d", &A);
		scanf("%d", &B);
		scanf("%d", &C);
	}

	printf("%d\n%d\n%d\n%d\n", (A+B)%C, (A%C + B%C)%C, (A*B)%C, (A%C*B%C)%C);

	return 0;

}
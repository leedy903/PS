#include <stdio.h>

int main(void) {
	int deci[10] = { 0, }; //from zero to nine
	int i = 0;
	int A = 0, B = 0, C = 0, result = 0;

	scanf("%d %d %d", &A, &B, &C);

	result = A*B*C;

	while(result) {
		deci[result % 10]++;
		result /= 10;
	}

	for (i = 0; i < 10; i++) {
		printf("%d\n", deci[i]);
	}

	return 0;

}
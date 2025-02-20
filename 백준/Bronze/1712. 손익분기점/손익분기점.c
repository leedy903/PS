#include <stdio.h>
int main(void) {
	int A, B, C = 0;
	scanf("%d %d %d", &A, &B, &C);
	printf("%d", B < C ? A / (C - B) + 1 : -1);
	return 0;
}
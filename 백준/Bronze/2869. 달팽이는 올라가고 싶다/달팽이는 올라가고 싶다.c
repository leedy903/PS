#include <stdio.h>
#include <math.h>
int main(void) {
	int A, B, V = 0;
	scanf("%d %d %d", &A, &B, &V);
	printf("%d", (int)ceil((double)(V - A) / (A - B)) + 1);
	return 0;
}

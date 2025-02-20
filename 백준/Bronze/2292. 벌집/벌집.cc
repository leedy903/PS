#include <stdio.h>
int main() {
	int i = 0, j = 0, N = 0;
	scanf("%d", &N);
	for (i = 1, j = 1; i < N; i += j*6, j++);
	printf("%d", j);
	return 0;
}
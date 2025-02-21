#include <stdio.h>
int main(void) {
	int i = 0, j = 0;
	int max = 0, N = 0;
	while (i++ < 9) {
		scanf("%d", &N);
		if (N > max) {
			max = N;
			j = i;
		}
	}
	printf("%d\n%d", max, j);
	return 0;
}

#include <stdio.h>

int main(void) {
	int i, j, N = 0;
	while (N < 1 || N > 100) {
		scanf("%d", &N);
	}

	for (i = 0; i < N; i++) {
        for (j = 0; j < i; j++) {
            printf(" ");
        }
        for (j = N; j > i; j--) {
			printf("*");
		}
        printf("\n");
	}

	return 0;
}
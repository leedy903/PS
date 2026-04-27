#include <stdio.h>
int main(void) {
	int i, j, k, N = 0;
	scanf("%d", &N);
	for(i = 0; i < N; i++){
		for(j = 0; j < i; j++) {
			printf(" ");
		}
		for(k = 2*(N - i) - 1 ; k > 0; k--) {
			printf("*");
		}
		printf("\n");
	}
	for(i = 2; i < N + 1; i++){
		for(j = N - i; j > 0; j--) {
			printf(" ");
		}
		for(k = 0; k < 2*i - 1; k++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int i, j, num = 0;
	scanf("%d", &num);
	for (i = 0; i < num; i++) {
		for (j = num-1; j > i; j--) {
			printf(" ");
		}
		for (j = 0; j < i+1; j++) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}
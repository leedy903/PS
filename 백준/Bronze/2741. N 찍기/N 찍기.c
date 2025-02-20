#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int i = 0,num = 0;
	scanf("%d", &num);
	for (i = 1; i <= num; i++) {
		printf("%d\n", i);
	}
	return 0;
}
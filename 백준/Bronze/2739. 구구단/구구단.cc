#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int i = 0,num = 0;
	scanf("%d", &num);
	for (i = 1; i < 10; i++) {
		printf("%d * %d = %d\n", num, i, num*i);
	}
	return 0;
}

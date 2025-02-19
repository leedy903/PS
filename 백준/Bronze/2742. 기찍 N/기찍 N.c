#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int i = 0,num = 0;
	scanf("%d", &num);
	for (i = 0; i < num; i++) {
		printf("%d\n", num-i);
	}
	return 0;
}
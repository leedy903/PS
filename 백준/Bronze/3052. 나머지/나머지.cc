#include <stdio.h>
int main(void) {
	int i = 0;
	int d = 0, count = 0;
	int rest[42] = { 0, };
	for (i = 0; i < 10; i++) {
		scanf("%d", &d);
		if (!rest[d % 42]) rest[d % 42] = 1;
	}
	for (i = 0; i < 42; i++) {
		if (rest[i]) count++;
	}
	printf("%d", count);
	return 0;
}
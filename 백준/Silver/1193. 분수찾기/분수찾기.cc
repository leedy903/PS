#include <stdio.h>
int main(void) {
	int i = 0, j = 1, X = 0;
	scanf("%d", &X);
	for (i = 1; j < X; i++, j += i);
	if (i % 2) printf("%d/%d", 1 + j - X, i - (j - X));
	else printf("%d/%d", i - (j - X), 1 + j - X);
	return 0;
}
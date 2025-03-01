#include <stdio.h>
int main(void) {
	int i = 0;
	int N = 0, min = 1000001, max = -1000001;
	scanf("%d", &N);
	while (N--) {
		scanf("%d", &i);
		if (i < min) min = i;
		if (i > max) max = i;
	}
	printf("%d %d", min, max);
	return 0;
}
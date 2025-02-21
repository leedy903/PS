#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int i, j, start, end;
	int total = 0, minp = -1;
	int plist[10000] = { 0 };

	// finding prime number
	for (i = 1; i <= 10000; i++) {
		for (j = 2; j < i; j++) {
			if (i%j == 0) {
				plist[i - 1] = 1;
				break;
			}
		}
	}
	plist[0] = 1;

	scanf("%d %d", &start, &end);

	// check the input number
	// if it is the prime total++ if not do nothing
	for (i = start; i <= end; i++) {
		if (plist[i - 1] == 0) {
			total += i;
			if (minp == -1) minp = i;
		}
	}
	if (minp == -1)
		printf("-1");
	else printf("%d\n%d", total, minp);


	return 0;
}
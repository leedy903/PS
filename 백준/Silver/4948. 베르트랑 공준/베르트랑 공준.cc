#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_NUM 246912

int main(void) {
	int i, j, size;
	int total = 0;
	int plist[MAX_NUM] = { 0 };

	// finding prime number
	for (i = 2; i <= MAX_NUM; i++) {
		plist[i] = i;
	}

	for (i = 2; i <= MAX_NUM; i++) {
		if (plist[i] == 0) continue;
		for (j = i + i; j <= MAX_NUM; j += i) plist[j] = 0;
	}

	while (1) {
		scanf("%d", &size);
		if (size == 0) break;
		// check the input number
		// if it is the prime total++ if not do nothing
		for (i = size; i < size * 2; i++) {
			if (plist[i + 1] != 0) total++;
		}
		printf("%d\n", total);
		total = 0;
	}
	return 0;
}
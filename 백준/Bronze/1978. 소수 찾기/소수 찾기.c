#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int i, j, size;
	int total = 0;
	int plist[1000] = { 0 }, list[100] = { 0 };

	// finding prime number
	for (i = 1; i <= 1000; i++) {
		for (j = 2; j < i; j++) {
			if (i%j == 0) {
				plist[i-1] = 1;
				break;
			}
		}
	}	
	plist[0] = 1;

	scanf("%d", &size);
	 
	for (i = 0; i < size; i++) {
		scanf("%d", &list[i]);
	}

	// check the input number
	// if it is the prime total++ if not do nothing
	for (i = 0; i < size; i++) {
		if (plist[list[i]-1] == 0) total++;
	}


	printf("%d", total);

	return 0;
}
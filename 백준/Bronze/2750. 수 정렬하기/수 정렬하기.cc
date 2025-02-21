#include <stdio.h>

int main(void) {
	int size, i, j, temp = 0;
	int list[1000];

	scanf("%d", &size);
	for (i = 0; i < size; i++) {
		scanf("%d", &list[i]);
	}

	for (i = 0; i < size - 1; i++) {
		for (j = 0; j < size - 1 -i; j++) {
			if (list[j] > list[j + 1]) {
				temp = list[j];
				list[j] = list[j + 1];
				list[j + 1] = temp;
			}
		}
	}
	
	for (i = 0; i < size; i++) {
		printf("%d\n", list[i]);
	}

	return 0;
}


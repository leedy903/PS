#include <stdio.h>

int main(void) {
	int i = 0, score = 0, total = 0;

	for (i = 0; i < 5; i++) {
		scanf("%d", &score);
		if (score < 40) score = 40;
		total += score;
	}

	printf("%d", total / 5);

	return 0;
}
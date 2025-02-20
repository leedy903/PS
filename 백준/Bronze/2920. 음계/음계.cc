#include <stdio.h>

int main(void) {
	int i = 0, a = 1, d = 2;
	int scale[8] = { 0, };

	for (i = 0; i < 8; i++) scanf("%d", &scale[i]);

	for (i = 0; i < 8; i++) {
		if (scale[i] != i + 1) a = 0;
		if (scale[7 - i] != i + 1) d = 0;
	}

	if (a) printf("ascending");
	else if (d) printf("descending");
	else printf("mixed");

	return 0;
}
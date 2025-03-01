#include <stdio.h>

int main(void) {
	int i = 0, j = 0, total = 0;
	char S[16] = { '\0', };
	scanf("%s", S);

	for (i = 0; S[i]; i++) {
		j = -1;
		while ((S[i] - j++ * 3) > 64);
		if (S[i] == 'S' || S[i] == 'V' || j == 10) j--;
		total += j + 1;
	}
	printf("%d", total);
	return 0;
}
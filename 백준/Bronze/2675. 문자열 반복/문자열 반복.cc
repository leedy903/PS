#include <stdio.h>

int main(void) {
	int T = 0, R = 0, i = 0, j = 0;
	char S[20] = { '\0', };

	scanf("%d", &T);
	
	while (T--) {
		scanf("%d", &R);
		scanf("%s", S);

		for (i = 0; S[i]; i++) {
			for (j = 0; j < R; j++) {
				printf("%c", S[i]);
			}
		}
		printf("\n");
	}

	return 0;
}
#include <stdio.h>
int main(void) {
	int N = 0, i = 0, count = 0;
	scanf("%d", &N);
	while (N--) {
		int isGroup[26] = { 0, }, nG = 0;
		char S[100] = { '\0' };
		scanf("%s", S);
		for (i = 0; S[i]; i++) {
			if (isGroup[S[i] - 'a'] == 1) {
				if (S[i] == S[i - 1]) continue;
				else nG = 1;
			}
			else isGroup[S[i] - 'a'] = 1;
		}
		if (!nG) count++;
	}
	printf("%d", count);
	return 0;
}
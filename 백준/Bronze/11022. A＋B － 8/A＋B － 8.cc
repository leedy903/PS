#include <stdio.h>
int main(void) {
	int i = 0;
	int T, A, B = 0;
	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		scanf("%d %d", &A, &B);
		printf("Case #%d: %d + %d = %d\n", i + 1, A, B, A + B);
	}
	return 0;
}
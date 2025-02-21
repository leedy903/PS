#include <stdio.h>
int main(void) {
	int T, H, W, N = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d %d", &H, &W, &N);
		printf("%d\n", (N + H) / H + (N%H ? N%H * 100 : H * 100 - 1));
	}
	return 0;
}

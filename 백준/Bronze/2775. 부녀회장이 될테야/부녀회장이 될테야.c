#include <stdio.h>
int main(void) {
	int i, j = 0;
	int t, k, n = 0;
	int arr[15][15] = { 1, };
	for (i = 0; i < 15; i++) arr[i][0] = i;
	for (i = 1; i < 15; i++) {
		for (j = 1; j < 15; j++) {
			arr[i][j] += arr[i - 1][j] + arr[i][j - 1];
		}
	}
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &k, &n);
		printf("%d\n", arr[n][k]);
	}
	return 0;
}
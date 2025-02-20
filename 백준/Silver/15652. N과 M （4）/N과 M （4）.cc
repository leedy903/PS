#include <stdio.h>

int N, M;
int arr[9] = { 0 };

void dfs(int cnt, int front) {
	int i = 0, j = 0;
	if (cnt == M) {
		for (i = 0; i < M; i++) {
			printf("%d ", arr[i]);
		}
		printf("\n");
	}
	else {
		for (i = 1; i <= N; i++) {
			if (front <= i) {
				arr[cnt] = i;
				dfs(cnt + 1, i);
			}
		}
	}
}

int main() {
	scanf("%d %d", &N, &M);
	dfs(0, 0);
}
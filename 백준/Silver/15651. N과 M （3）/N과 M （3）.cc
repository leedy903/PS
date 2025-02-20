#include <stdio.h>

int N, M;
int arr[9] = { 0 };

void dfs(int cnt) {
	int i = 0;
	if (cnt == M) {
		for (i = 0; i < M; i++) {
			printf("%d ", arr[i]);
		}
		printf("\n");
	}
	else {
		for (i = 1; i <= N; i++) {
			arr[cnt] = i;
			dfs(cnt + 1);
		}
	}
}

int main() {
	scanf("%d %d", &N, &M);
	dfs(0);
}
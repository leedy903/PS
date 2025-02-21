#include <stdio.h>

void star(int n, int x, int y);

char starmatrix[3072][6144];

int main(void) {
	int i = 0, j = 0, n = 0;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		for (j = 0; j < 2 * n; j++) {
			starmatrix[i][j] = ' ';
		}
	}

    star(n, n - 1, 0);
	
    for (i = 0; i < n; i++) {
		for (j = 0; j < 2 * n; j++) {
			printf("%c", starmatrix[i][j]);
		}
		printf("\n");
	}
	
    return 0;
}

void star(int n, int x, int y) {
	if (n == 3) {
		starmatrix[y][x] = '*';
		starmatrix[y + 1][x - 1] = '*';
		starmatrix[y + 1][x + 1] = '*';
		starmatrix[y + 2][x - 2] = '*';
		starmatrix[y + 2][x - 1] = '*';
		starmatrix[y + 2][x] = '*';
		starmatrix[y + 2][x + 1] = '*';
		starmatrix[y + 2][x + 2] = '*';
		return;
	}
	else {
		star(n / 2, x, y);
		star(n / 2, x - (n / 2), y + (n / 2));
		star(n / 2, x + (n / 2), y + (n / 2));
	}
}
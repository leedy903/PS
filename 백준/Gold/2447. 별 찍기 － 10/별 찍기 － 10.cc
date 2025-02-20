#include <stdio.h>

// n : time, x: wide, y: height
void star(int n, int x, int y);

char paper[6562][6562];

int main(void) {
	int i = 0, j = 0;
	int n = 0, x = 0, y = 0;

	scanf("%d", &n);

	// init the array
	for (i = 0; i < n; i++) {
		for (j = 0; j < n + 1; j++) {
			if (j == n) paper[i][j] = '\0';
			else paper[i][j] = ' ';
		}
	}
    
	star(n, (n - 1)/2, (n - 1)/2);

	// print the array
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			printf("%c", paper[i][j]);
		}
		printf("\n");
	}

	return 0;
}

void star(int n, int x, int y) {
	int i = 0, j = 0;

	if (n == 3) {
		paper[y - 1][x - 1] = '*';
		paper[y - 1][x] = '*';
		paper[y - 1][x + 1] = '*';
		paper[y][x - 1] = '*';
		paper[y][x + 1] = '*';
		paper[y + 1][x - 1] = '*';
		paper[y + 1][x] = '*';
		paper[y + 1][x + 1] = '*';
		return;
	}

	n = n / 3;
	star(n, x - n, y - n);
	star(n, x, y - n);
	star(n, x + n, y - n);
	star(n, x - n, y);
	star(n, x + n, y);
	star(n, x - n, y + n);
	star(n, x, y + n);
	star(n, x + n, y + n);
}
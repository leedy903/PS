#include <stdio.h>
#include <math.h>
void move(int from, int to);
void hanoi(int n, int from, int to, int use);
int main(void) {
	int n = 0;
	scanf("%d", &n);
	printf("%d\n", (int)pow(2, n) - 1);
	hanoi(n, 1, 2, 3);
	return 0;
}
void move(int from, int to) {
	printf("%d %d\n", from, to);
}
void hanoi(int n, int from, int use, int to) {
	if (n == 1) move(from, to);
	else {
		hanoi(n - 1, from, to, use);
		move(from, to);
		hanoi(n - 1, use, from, to);
	}
}
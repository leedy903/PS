#include <stdio.h>

int isHansu(int n);
int main(void) {
	int i, size, num = 0;
	scanf("%d", &size);
	for (i = 1; i < size + 1; i++) {
		if (i < 100) num = i;
		else if (i == 1000) break;
		else
			if (isHansu(i)) num++;

	}
	printf("%d", num);
	return 0;
}

int isHansu(int n) {
	int i;
	int arr[3];
	for (i = 0; i < 3; i++) {
		arr[i] = n % 10;
		n = n / 10;
	}
	if (arr[2] - arr[1] == arr[1] - arr[0]) return 1;
	else return 0;
}
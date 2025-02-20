#include <stdio.h>
int main(void) {
	int y = 0;
	scanf("%d", &y);
	printf("%d", (((!(y % 4) && y % 100) || !(y % 400))));
	return 0;
}
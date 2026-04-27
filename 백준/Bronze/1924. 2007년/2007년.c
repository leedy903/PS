#include <stdio.h>

int main(void) {

	int x = 0, y = 0, sum = 0, i;
	int months[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };

	while (x < 1 || x > 12 || y < 1 || y > 31) {
		scanf("%d %d", &x, &y);
	}

	for (i = 0; i < x - 1; i++) {
		sum += months[i];
	}

	sum += y;

	if ((sum % 7) == 0) printf("SUN");
	else if ((sum % 7) == 1) printf("MON");
	else if ((sum % 7) == 2) printf("TUE");
	else if ((sum % 7) == 3) printf("WED");
	else if ((sum % 7) == 4) printf("THU");
	else if ((sum % 7) == 5) printf("FRI");
	else if ((sum % 7) == 6) printf("SAT");
	else return 0;

	return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(void) {
	int T = 0, i = 0;
	int *result;
	scanf("%d", &T);
	result = (int*)malloc(sizeof(int)*T);
	for (i = 0; i < T; i++) {
		int x = 0, y = 0, count = 0, m = 0;
		double d = 0;
		double t = 0;
		scanf("%d %d", &x, &y);
		d = (double) y - x;
		t = sqrt(d);
		m = (int)t;
		if (t > (double)m) m++;
		if ((int)d > m*m - m) result[i] = 2 * m - 1;
		else result[i] = 2*m - 2;
	}	
	for (i = 0; i < T; i++) printf("%d\n", result[i]);
	return 0;
}
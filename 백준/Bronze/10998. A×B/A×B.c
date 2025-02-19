#include <stdio.h>

int main(void){
    int A = -1, B = 11;
	while (A <= 0 || B >= 10)
		scanf("%d %d", &A , &B);
	printf("%d\n", A*B);
	return 0;
}
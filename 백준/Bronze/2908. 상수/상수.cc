#include <stdio.h>
int main(void) {
	int A= 0, B = 0, RA = 0, RB = 0;
	scanf("%d %d", &A, &B);
	while (A) {RA = RA * 10 + A % 10; A /= 10;}
	while (B) {RB = RB * 10 + B % 10; B /= 10;}
	RA < RB ? printf("%d", RB) : printf("%d", RA);
	return 0;
}
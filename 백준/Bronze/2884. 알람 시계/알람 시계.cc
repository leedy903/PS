#include <stdio.h>
int main(void) {
	int H, M = 0;
	int TH, TM = 0;
	scanf("%d %d", &H, &M);
	if ((TM = M - 45) < 0) {
		TM = 60 + TM;
		if ((TH = H - 1) < 0) TH = 24 + TH;
	}
    else TH = H;
	printf("%d %d", TH, TM);
	return 0;
}
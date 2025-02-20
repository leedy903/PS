#include <stdio.h>
int check(char* p) {
	int i, sum = 0;
	for (i = 0; p[i]; i++) {
		p[i] == '(' ? sum++ : sum--;
		if (sum < 0) return 0;
	}
	return sum == 0 ? 1 : 0;
}
int main(void) {
	int T = 0;
	char p[55];
	scanf("%d", &T);
	while (T--) {
		scanf("%s", p);
		check(p) ? printf("YES\n") : printf("NO\n");
	}
	return 0;
}
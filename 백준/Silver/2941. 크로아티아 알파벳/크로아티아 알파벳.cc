#include <stdio.h>

int check(char * s, int i);
int main(void) {
	int i = 0, n = 0, t = 0;
    char S[100] = { '\0' };

	scanf("%s", S);

	for (i = 0; S[i]; i++) {
		if ((n = check(S, i)) - i) {
			t += n - i;
			i = n;
		}
	}

	printf("%d", i - t);

	return 0;
}

int check(char * s, int i) {
	if (s[i] == 'c' && s[i + 1] == '=') return i + 1;
	else if (s[i] == 'c' && s[i + 1] == '-') return i + 1;
	else if (s[i] == 'd' && s[i + 1] == 'z' && s[i + 2] == '=') return i + 2;
	else if (s[i] == 'd' && s[i + 1] == '-') return i + 1;
	else if (s[i] == 'l' && s[i + 1] == 'j') return i + 1;
	else if (s[i] == 'n' && s[i + 1] == 'j') return i + 1;
	else if (s[i] == 's' && s[i + 1] == '=') return i + 1;
	else if (s[i] == 'z' && s[i + 1] == '=') return i + 1;
	else return i;
}
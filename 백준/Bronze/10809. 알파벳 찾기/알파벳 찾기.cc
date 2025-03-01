#include <stdio.h>
#include <string.h>

int main(void) {
	int i = 0;
	char S[100];
	int Alpa[26];

	memset(S, '\0', sizeof(S));
	memset(Alpa, -1, sizeof(Alpa));

	scanf("%s", S);
	
	for (i = 0; S[i]; i++) {
		if (Alpa[(int)S[i] - 97] == -1) Alpa[(int)S[i]-97] = i;
	}

	for (i = 0; i < 26; i++) {
		printf("%d ", Alpa[i]);
	}
	
	return 0;
}
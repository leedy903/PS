#include <stdio.h>

int main(void) {
	int i = 0, max = 0, index = 0, temp = 0;
	int count[26] = { 0, };
	char S[1000000] = { '\0', };

	scanf("%s", S);

	for (i = 0; S[i]; i++) {
		if ((int)S[i] < 91) count[(int)S[i] + 32 - 97]++;
		else count[(int)S[i] - 97]++;
	}

	for (i = 0; i < 26; i++) {
		if (max < count[i]) {
			max = count[i];
			index = i;
		}
		else if (max == count[i]) temp = i;
	}
	if (temp > index) printf("?");
	else printf("%c", (char)(index + 65));

	return 0;
}
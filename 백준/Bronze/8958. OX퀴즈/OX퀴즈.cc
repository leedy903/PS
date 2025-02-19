#include <stdio.h>
#include <string.h>

int main(void) {
	int i = 0, tsize = 0, score = 0, total = 0;
	char result[80];

	scanf("%d", &tsize);

	while (tsize--) {
		scanf("%s", result);
		for (i = 0; result[i]; i++) {
			if (result[i] == 'O') score++;
			else {
				while (score) total += score--;
			}
		}
		while (score) total += score--;
		printf("%d\n", total);
		memset(result, '\0', sizeof(result));
		total = 0;
		score = 0;
	}
	return 0;
}
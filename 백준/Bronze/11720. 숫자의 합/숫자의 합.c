#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int i, size, total = 0;
	char num[100];
	
	scanf("%d", &size);
	
	//*num = malloc(sizeof(char)*size);
	scanf("%s", num);
	
	for (i = 0; i < size; i++) {
		//total += atoi(num[i]);
		total += (int)num[i]-48;
	}
	printf("%d", total);

	return 0;
}
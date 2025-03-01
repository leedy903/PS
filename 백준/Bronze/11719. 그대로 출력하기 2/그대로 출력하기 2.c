#include <stdio.h>
#include <string.h>

int main(void) {

	char sentences[101];
	
	// we don't use scanf() because we have 'space' in the sentences.
	
	while (fgets(sentences, sizeof(sentences), stdin))
		printf("%s", sentences);

	return 0;
}
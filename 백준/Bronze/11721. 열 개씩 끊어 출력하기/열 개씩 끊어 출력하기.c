#include <stdio.h>
#include <string.h>

int main (void) {
    
    int i = 0;
    char input [100] = {0};

    scanf("%s", input);

    while (input[i++] != '\0') {
        printf("%c", input[i-1]);
        if (!(i%10)) printf("\n");
    }

    return 0;

}
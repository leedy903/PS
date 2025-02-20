#include <stdio.h>

int main (void) {
    int num[3] = { 0 }, i = 0, j = 0, t = 0;

    scanf("%d %d %d", &num[0], &num[1], &num[2]);

    // bubble sort
    for( j = 0; j < 2; j++ ) {
        for( i = 0; i < 2; i++ ) {
            if (num[i] > num[i+1]) {
                t = num[i];
                num[i] = num[i + 1];
                num[i + 1] = t;
            }
        }
    }

    printf("%d\n", num[1]);

    return 0;
}
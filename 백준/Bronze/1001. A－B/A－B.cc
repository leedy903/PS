#include <stdio.h>

int main (void) {
    int A = 0, B = 10;
    while (A <= 0)
        scanf("%d", &A);
    while (B >= 10)
        scanf("%d", &B);   
    printf("%d", A-B);
    
    return 0;
}
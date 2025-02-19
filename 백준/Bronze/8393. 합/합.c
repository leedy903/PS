#include <stdio.h>

int main (void) {
    int n = 0, sum = 0;
    
    while (n < 1 || n > 10000)
        scanf("%d", &n);
    
    while (n)
        sum += n--; 
    
    printf("%d", sum);
    
    return 0;
}
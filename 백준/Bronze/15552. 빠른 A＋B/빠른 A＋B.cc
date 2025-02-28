#include <stdio.h>

int main(void) {
    
    int T = 0, A = 0, B = 0;
    
    scanf("%d", &T);
    
    while(T--){
        scanf("%d %d", &A, &B);
        printf("%d\n", A+B);
    }
    
    return 0;
}
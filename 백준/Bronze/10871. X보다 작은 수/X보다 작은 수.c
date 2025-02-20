#include <stdio.h>

int main (void) {
    int N = 0, X = 0, i = 0, t = 0;
    int A[10000] = {0};

    scanf("%d %d", &N, &X);

    while(N--) {
        scanf("%d", &t);
        if (t < X) A[i++] = t;
    }

    i = 0;

    while(A[i]) printf("%d ", A[i++]);

    return 0;
}
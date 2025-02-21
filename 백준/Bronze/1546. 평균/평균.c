#include <stdio.h>

int main(void) {
    int N = 0, M = 0, i = 0;
    double avg = 0;
    double score[1000] = { 0 };
    
    scanf("%d", &N);
    for (i = 0; i < N; i++) {
        scanf("%lf", &score[i]);
        if (score[i] > M) M = score[i];
    }
    for (i = 0; i < N; i++) avg += score[i]/M*100;
    
    printf("%.2lf", avg/N);

}
#include <stdio.h>

int main (void) {
    int C = 0, N = 0, i = 0;
    double avg = 0, count = 0;
    int score[1000] = { 0 };

    scanf("%d", &C);

    while(C--) {
        scanf("%d", &N);
        
        for (i = 0; i < N; i++) scanf("%d", &score[i]);

        for (i = 0; i < N; i++) avg += score[i];

        avg = avg/N;

        for (i = 0; i < N; i++) {
            if (score[i] > avg) count++;
        }

        printf("%.3lf%\n", count/N*100);

        avg = 0;
        count = 0;

    }
    return 0;
}
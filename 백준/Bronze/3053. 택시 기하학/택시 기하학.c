#include <stdio.h>
int main(void) {
    int r = 0;
    scanf("%d", &r);
    printf("%.6lf\n%.6lf", 3.14159265358979*r*r,2.0*r*r);
    return 0;
}
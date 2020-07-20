#include <stdio.h>
#include <math.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 20                   | 
 | 14264 정육각형과 삼각형     | 
 ---------------------------- 
*/

int main(){
    int L;

    scanf("%d", &L);

    printf("%.10lf", (3 * sqrt(3) * pow(L, 2) / 12));
    return 0;
}

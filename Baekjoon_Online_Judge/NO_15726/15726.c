#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 15726 이칙연산            | 
 ---------------------------- 
*/

int main(){
    double A, B, C, res1, res2;

    scanf("%lf %lf %lf", &A, &B, &C);

    res1 = A * B / C;
    res2 = A / B * C;

    printf("%d", res1 > res2 ? (int)res1 : (int)res2);

    return 0;
}

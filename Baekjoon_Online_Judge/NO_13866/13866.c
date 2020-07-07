#include <stdio.h>
#include <math.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 13866 팀 나누기           | 
 ---------------------------- 
*/

int main(){
    int A, B, C, D;

    scanf("%d %d %d %d", &A, &B, &C, &D);
    printf("%d", abs(D + A - C - B));
    return 0;
}
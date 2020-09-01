#include <stdio.h>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 구구단                             | 
 -------------------------------------- 
*/

int main(){
    int N;

    scanf("%d", &N);

    for (int i = 1; i <= 9; i ++) printf("%d * %d = %d\n", N, i, N * i);
    return 0;
}
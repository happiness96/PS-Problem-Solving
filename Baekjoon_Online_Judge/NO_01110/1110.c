#include <stdio.h>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 더하기 사이클                       | 
 -------------------------------------- 
*/

int main(){
    int N, ori, cycle_length = 0;

    scanf("%d", &N);
    ori = N;

    while (1){
        cycle_length ++;
        N = N % 10 * 10 + (N / 10 + N % 10) % 10;

        if (N == ori) break;
    }

    printf("%d", cycle_length);
    
    return 0;
}
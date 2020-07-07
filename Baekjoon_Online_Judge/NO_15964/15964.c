#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 15964 이상한 기호          | 
 ---------------------------- 
*/

int main(){
    long long A, B;

    scanf("%lld %lld", &A, &B);
    printf("%lld", (A + B) * (A - B));
    return 0;
}

#include <stdio.h>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 세 수                              | 
 -------------------------------------- 
*/

int main(){
    int A, B, C;

    scanf("%d %d %d", &A, &B, &C);

    if (A > B){
        int tmp = A;
        A = B;
        B = tmp;
    }

    if (B > C){
        int tmp = B;
        B = C;
        C = tmp;
    }

    if (A > B){
        int tmp = A;
        A = B;
        B = tmp;
    }

    printf("%d", B);
    
    return 0;
}
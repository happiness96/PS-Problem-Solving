#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 20                   | 
 | 3507 Automated Telephone Exchange| 
 ---------------------------- 
*/

int main(){
    int n, cnt = 0;

    scanf("%d", &n);

    for(int num1 = 0; num1 < 100; num1 ++){
        for(int num2 = 0; num2 < 100; num2 ++){
            if(n - num1 - num2 == 0) cnt ++;
        }
    }

    printf("%d", cnt);
    return 0;
}

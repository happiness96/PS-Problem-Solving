#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 19                   | 
 | 5522 카드 게임            | 
 ---------------------------- 
*/

int main(){
    int total = 0;

    for(int i = 0; i < 5; i++){
        int number;
        scanf("%d", &number);

        total += number;
    }

    printf("%d", total);
    return 0;
}

#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 11908 카드                | 
 ---------------------------- 
*/

int main(){
    int n, total = 0, maxi = 0;

    scanf("%d", &n);

    for(int i = 0; i < n; i ++){
        int c;

        scanf("%d", &c);
        total += c;

        if (maxi < c) maxi = c;
    }

    printf("%d", total - maxi);
    
    return 0;
}

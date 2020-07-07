#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 9664 NASLJEDSTVO         | 
 ---------------------------- 
*/

int main(){
    int N, O, mini = 2147483647, maxi = 0;

    scanf("%d %d", &N, &O);

    for(int num = 1; num <= O * 2; num ++){
        if(num - num / N == O){
            if(mini > num) mini = num;
            if(maxi < num) maxi = num;
        }
    }

    printf("%d %d", mini, maxi);

    return 0;
}

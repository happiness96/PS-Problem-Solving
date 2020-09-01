#include <stdio.h>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 최댓값                             | 
 -------------------------------------- 
*/

int main(){
    int numbers[9], result = 0, result_ind;

    for (int i = 0; i < 9; i ++) scanf("%d", &numbers[i]);

    for(int i = 0; i < 9; i ++){
        if (numbers[i] > result){
            result = numbers[i];
            result_ind = i + 1;
        }
    }

    printf("%d\n", result);
    printf("%d", result_ind);
    return 0;
}
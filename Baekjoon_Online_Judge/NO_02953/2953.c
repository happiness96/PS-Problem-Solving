#include <stdio.h>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2021                          | 
 | Month 01                           | 
 | Day 01                             | 
 | 2953 나는 요리사다                  | 
 -------------------------------------- 
*/

int main(){
    int score[5] = {0, }, max_score = 0, winner = 0;

    for(int i = 0; i < 5; i ++){
        for(int j = 0; j < 4; j ++){
            int s;
            scanf("%d", &s);
            score[i] += s;
        }
    }
    
    for(int i = 0; i < 5; i ++){
        if(score[i] > max_score){
            max_score = score[i];
            winner = i + 1;
        }
    }

    printf("%d %d", winner, max_score);
    return 0;
}
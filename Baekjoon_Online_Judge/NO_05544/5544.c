#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 27                   | 
 | 5544 심부름 가는 길        | 
 ---------------------------- 
*/

int main(){
    int total_min = 0, total_sec = 0;

    for(int i = 0; i < 4; i ++){
        int time;

        scanf("%d", &time);

        total_sec += time;
    }

    total_min += total_sec / 60;
    total_sec %= 60;

    printf("%d\n%d", total_min, total_sec);
    return 0;
}

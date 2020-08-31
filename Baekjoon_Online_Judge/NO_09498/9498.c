#include <stdio.h>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 08                           | 
 | Day 31                             | 
 | 시험 성적                              | 
 -------------------------------------- 
*/

int main(){
    int score;

    scanf("%d", &score);

    if (90 <= score && score <= 100) printf("A");
    else if (80 <= score && score <= 89) printf("B");
    else if (70 <= score && score <= 79) printf("C");
    else if (60 <= score && score <= 69) printf("D");
    else printf("F");

    return 0;
}
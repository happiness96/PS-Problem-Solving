#include <stdio.h>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 02                             | 
 | 단어 공부                           | 
 -------------------------------------- 
*/

int main(){
    char string[1000000];
    int counting[26];

    scanf("%s", &string);

    for (int i = 0; string[i] != '\0'; i ++){
        if (string[i] >= 'a') string[i] -= 32;

        counting[string[i] - 'A'] ++;
    }

    int max_count = 0;
    char res;

    for (int i = 0; i < 26; i ++){
        if (counting[i] > max_count){
            max_count = counting[i];
            res = i + 'A';
        }

        else if (counting[i] == max_count) res = '?';
    }

    printf("%c", res);

    return 0;
}
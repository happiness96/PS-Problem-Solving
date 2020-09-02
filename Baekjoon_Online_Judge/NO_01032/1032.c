#include <stdio.h>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 02                             | 
 | 명령 프롬프트                       | 
 -------------------------------------- 
*/

int main(){
    int N;
    char form[50];

    scanf("%d", &N);
    scanf("%s", &form);

    for (int i = 0; i < N - 1; i ++){
        char sub_s[50];

        scanf("%s", &sub_s);

        for (int ind = 0; sub_s[ind] != '\0'; ind ++){
            if (sub_s[ind] != form[ind]) form[ind] = '?';
        }
    }

    printf("%s", form);

    return 0;
}
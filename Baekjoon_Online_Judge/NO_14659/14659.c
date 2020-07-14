#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 14659 한조서열정리하고옴ㅋㅋ | 
 ---------------------------- 
*/

int main(){
    int N, max_height = 0, cnt = 0, result = 0;

    scanf("%d", &N);

    for(int i = 0; i < N; i ++){
        int height;

        scanf("%d", &height);

        if(height > max_height){
            max_height = height;
            result = result < cnt ? cnt : result;
            cnt = 0;
        }
        else cnt ++;
    }

    printf("%d", result < cnt ? cnt : result);
    return 0;
}

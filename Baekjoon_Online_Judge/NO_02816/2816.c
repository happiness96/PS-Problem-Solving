#include <stdio.h>
#include <string.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 15                   | 
 | 2816 디지털 티비           | 
 ---------------------------- 
*/

int main(){
    int N, KBS1, KBS2;

    scanf("%d", &N);

    for(int ind = 0; ind < N; ind ++){
        char channel[11];
        
        scanf("%s", &channel);
        
        if(strcmp(channel, "KBS1") == 0) KBS1 = ind;
        else if(strcmp(channel, "KBS2") == 0) KBS2 = ind;
    }

    for(int i = 0; i < KBS1; i ++) printf("1");
    for(int i = 0; i < KBS1; i ++) printf("4");

    if(KBS2 < KBS1) KBS2 ++;

    for(int i = 0; i < KBS2; i ++) printf("1");
    for(int i = 0; i < KBS2 - 1; i ++) printf("4");

    return 0;
}

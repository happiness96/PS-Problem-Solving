#include <stdio.h>
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 18247 겨울왕국 티켓 예매    | 
 ---------------------------- 
*/

int main(){
    int T;

    scanf("%d", &T);

    for(int i = 0; i < T; i ++){
        int N, M;

        scanf("%d %d", &N, &M);

        if(N < 12 || M < 4) printf("-1\n");
        else printf("%d\n", 11 * M + 4);
    }
    
    return 0;
}

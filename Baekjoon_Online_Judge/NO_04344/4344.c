#include <stdio.h>
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 평균은 넘겠지                      | 
 -------------------------------------- 
*/

int main(){
    int C;
    scanf("%d", &C);

    for (int i = 0; i < C; i ++){
        int N;
        scanf("%d", &N);

        int scores[N], total = 0;

        for (int i = 0; i < N; i ++){
            scanf("%d", &scores[i]);
            total += scores[i];
        }

        double avg = total / N;
        int over_avg = 0;

        for (int i = 0; i < N; i ++){
            if (scores[i] > avg) over_avg ++;
        }

        printf("%.3lf%%\n", (double)over_avg / N * 100);
    }

    return 0;
}
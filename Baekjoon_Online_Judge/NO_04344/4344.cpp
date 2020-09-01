#include <iostream>
#include <algorithm>
using namespace std;
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
    cin >> C;

    for (int i = 0; i < C; i ++){
        int N;
        cin >> N;

        int scores[N], total = 0;
        for (int j = 0; j < N; j ++){
            cin >> scores[j];
            total += scores[j];
        }

        double avg = total / N;
        int over_avg = 0;

        for (auto score: scores){
            if (score > avg) over_avg ++;
        }

        printf("%.3f%%\n", (double)over_avg / N * 100);
    }
    
    return 0;
}
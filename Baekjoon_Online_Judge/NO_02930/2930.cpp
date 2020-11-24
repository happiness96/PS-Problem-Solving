#include <iostream>
#include <algorithm>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 11                           | 
 | Day 24                             | 
 | 2930 가위 바위 보                   | 
 -------------------------------------- 
*/

int main(){
    int R, N, score = 0, max_score = 0;
    string SG;

    cin >> R >> SG >> N;

    int save[R][3] = {{0,}};

    for(int i = 0; i < N; i ++){
        string fr;
        cin >> fr;

        for(int j = 0; j < R; j ++){
            int ind = 0;
            if(fr[j] == 'S') ind = 1;
            if(fr[j] == 'P') ind = 2;

            save[j][ind] ++;

            if(fr[j] == SG[j]) score ++;
            else if(SG[j] == 'R' && fr[j] == 'S' || SG[j] == 'S' && fr[j] == 'P' || SG[j] == 'P' && fr[j] == 'R') score += 2;
        }
    }

    for(int j = 0; j < R; j ++){
        max_score += max(max(save[j][0] + save[j][1] * 2, save[j][1] + save[j][2] * 2), save[j][2] + save[j][0] * 2);
    }

    cout << score << '\n' << max_score;

    return 0;
}
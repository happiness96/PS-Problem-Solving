#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 2890 카약                 | 
 ---------------------------- 
*/

int main(){
    int R, C, rank = 1, res[10] = {0,};
    char board[51][51];

    cin >> R >> C;

    for(int i = 0; i < R; i ++){
        for(int j = 0; j < C; j ++) cin >> board[i][j];
    }

    for(int col = C - 2; col > 0; col --){
        int flag = 0;

        for(int row = 0; row < R; row ++){
            char val = board[row][col];
            
            if('1' <= val <= '9'){
                if(res[(int)val - '0'] == 0){
                    res[(int)val - '0'] = rank;
                    flag = 1;
                }
            }
        } 
        rank += flag;
    }

    for(int i = 1; i < 10; i ++) cout << res[i] << "\n";

    return 0;
}

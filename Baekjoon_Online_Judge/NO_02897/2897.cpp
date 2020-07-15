#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 15                   | 
  2897 몬스터 트럭            | 
 ---------------------------- 
*/

int main(){
    int R, C;

    cin >> R >> C;

    char board[R][C];

    for(int row = 0; row < R ; row ++){
        for(int col = 0; col < C; col ++){
            cin >> board[row][col];
        }
    }

    int res[5] = {0,};

    for(int row = 0; row < R - 1; row ++){
        for(int col = 0; col < C - 1; col ++){
            int cnt = 0;

            if(board[row][col] == 'X') cnt ++;
            if(board[row + 1][col] == 'X') cnt ++;
            if(board[row][col + 1] == 'X') cnt ++;
            if(board[row + 1][col + 1] == 'X') cnt ++;

            if(board[row][col] == '#') continue;
            if(board[row + 1][col] == '#') continue;
            if(board[row][col + 1] == '#') continue;
            if(board[row + 1][col + 1] == '#') continue;

            res[cnt] ++;
        }
    }

    for(int i = 0; i < 5; i ++) cout << res[i] << "\n";

    return 0;
}

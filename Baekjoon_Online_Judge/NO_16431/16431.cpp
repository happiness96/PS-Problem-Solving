#include <iostream>
#include <cmath>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 27                   | 
 | 16431 베시와 데이지        | 
 ---------------------------- 
*/

int main(){
    int b_row, b_col, d_row, d_col, j_row, j_col, b_distance, d_distance;

    cin >> b_row >> b_col >> d_row >> d_col >> j_row >> j_col;

    b_distance = abs(j_row - b_row) + abs(j_col - b_col);
    d_distance = abs(j_row - d_row) + abs(j_col - d_col);

    b_distance -= min(abs(j_row - b_row), abs(j_col - b_col));

    if(b_distance < d_distance) cout << "bessie";
    else if(b_distance > d_distance) cout << "daisy";
    else cout << "tie";

    return 0;
}

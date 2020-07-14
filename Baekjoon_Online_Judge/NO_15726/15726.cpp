#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 15726 이칙연산            | 
 ---------------------------- 
*/

int main(){
    double A, B, C, res1, res2;

    cin >> A >> B >> C;

    res1 = A * B / C;
    res2 = A / B * C;

    if(res1 > res2) cout << (int)res1;
    else cout << (int)res2;

    return 0;
}

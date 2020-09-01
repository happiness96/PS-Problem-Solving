#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 구구단                             | 
 -------------------------------------- 
*/

int main(){
    int N;

    cin >> N;

    for (int i = 1; i <= 9; i ++) cout << N << " * " << i << " = " << N * i << '\n';

    return 0;
}
#include <iostream>
#include "math.h"
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 20                   | 
 | 14264 정육각형과 삼각형     | 
 ---------------------------- 
*/

int main(){
    int L;
    cin >> L;
    cout.precision(12);
    cout << ((3 * sqrt(3) * pow(L, 2)) / 2) / 6;
    return 0;
}

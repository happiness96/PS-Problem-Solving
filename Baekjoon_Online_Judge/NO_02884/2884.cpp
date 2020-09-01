#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 08                           | 
 | Day 31                             | 
 | 알람 시계                          | 
 -------------------------------------- 
*/

int main(){
    int H, M;

    cin >> H >> M;

    M -= 45;

    if (M < 0){
        M += 60;
        H --;
    }

    if (H < 0) H += 24;

    cout << H << ' ' << M;
    
    return 0;
}
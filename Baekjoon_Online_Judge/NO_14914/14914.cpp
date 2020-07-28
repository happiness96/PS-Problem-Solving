#include <iostream>
#include <cmath>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 14914 사과와 바나나 나눠주기 | 
 ---------------------------- 
*/

int main(){
    int a, b;

    cin >> a >> b;

    for(int i = 1; i <= min(a, b); i ++){
        if(a % i == 0 and b % i == 0){
            cout << i << ' ' << a / i << ' ' << b / i << endl;
        }
    }

    return 0;
}

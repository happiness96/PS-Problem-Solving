#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 08                 | 
 | Day 02                   | 
 | 8393 합                  | 
 ---------------------------- 
*/

int main(){
    int n, total = 0;

    cin >> n;

    for(int i = 1; i <= n; i ++) total += i;

    cout << total;
    
    return 0;
}

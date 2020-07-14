#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 10280 Pizza voting       | 
 ---------------------------- 
*/

int main(){
    int n, p, start, end;

    cin >> n >> p;

    start = n / 3 + 1;
    end = start + (n - 1) / 3;

    if(start <= p and p <= end) cout << "YES";
    else cout << "NO";

    return 0;
}

#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 07                   | 
 | 11908 카드                | 
 ---------------------------- 
*/

int main(){
    int n, total = 0, maxi = 0;

    cin >> n;

    for (int i = 0; i < n; i ++){
        int c;

        cin >> c;
        total += c;

        if (c > maxi) maxi = c;
    }
    cout << total - maxi;

    return 0;
}

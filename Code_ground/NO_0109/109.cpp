#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 잔돈                     | 
 ---------------------------- 
*/

int main(){
    int T;

    cin >> T;

    for(int testcase = 1; testcase <= T; testcase ++){
        int rem, res1 = 0, res2 = 0, res3 = 0, res4 = 0;

        cin >> rem;

        cout << "Case #" << testcase << endl;

        res4 += rem / 500;
        rem %= 500;
        res3 += rem / 100;
        rem %= 100;
        res2 += rem / 50;
        rem %= 50;
        res1 += rem / 10;

        cout << res1 << " " << res2 << " " << res3 << " " << res4 << endl;
    }
    return 0;
}

#include <iostream>
#include <algorithm>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 햄버거                    | 
 ---------------------------- 
*/

int main(){
    int T;

    cin >> T;

    for(int testcase = 1; testcase <= T; testcase ++){
        int cnt1, cnt2, cnt3;

        cin >> cnt1 >> cnt2 >> cnt3;
        cout << "Case #" << testcase << endl;

        int tmp = min(cnt1 / 2, cnt2);
        cout << min(tmp, cnt3 / 3) << endl;
    }
    return 0;
}

#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 24                   | 
 | 플레이버튼                 | 
 ---------------------------- 
*/

int main(){
    int T;

    cin >> T;

    for(int testcase = 1; testcase <= T; testcase ++){
        int subscriber;

        cin >> subscriber;

        cout << "Case #" << testcase << endl;
        if(subscriber < 100000) cout << "NONE" << endl;
        else if(subscriber < 1000000) cout << "SILVER" << endl;
        else if(subscriber < 10000000) cout << "GOLD" << endl;
        else cout << "DIAMOND" << endl;
    }
    return 0;
}

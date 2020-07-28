#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 1비트 개수 세기            | 
 ---------------------------- 
*/

int main(){
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    int T;

    cin >> T;
    

    for(int testcase = 1; testcase <= T; testcase ++){
        int N, res = 0;
        
        cin >> N;

        for(int mul = 29; mul >= 0; mul --) res += N >> mul & 1;

        cout << "Case #" << testcase << "\n";
        cout << res << endl;
    }
    return 0;
}

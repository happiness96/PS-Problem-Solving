#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 08                           | 
 | Day 07                             | 
 | 스타벅스                           | 
 -------------------------------------- 
*/

int main(){
    int T;

    cin >> T;

    for(int testcase = 1; testcase <= T; testcase ++){
        int N, M, K;

        cin >> N >> M >> K;

        int what_do_you_want[N], coffee_cost[M], total = 0;

        for(int i = 0; i < N; i ++) cin >> what_do_you_want[i];
        for(int i = 0; i < M; i ++) cin >> coffee_cost[i];

        for(auto i_want_this: what_do_you_want) total += coffee_cost[i_want_this - 1];

        cout << "Case #" << testcase << "\n";
        
        if(total > K) cout << "N\n";
        else cout << "Y\n";
    }
    return 0;
}
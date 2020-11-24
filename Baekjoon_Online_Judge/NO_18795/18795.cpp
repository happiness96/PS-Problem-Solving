#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 11                           | 
 | Day 24                             | 
 | 18795 이동하기 3                    | 
 -------------------------------------- 
*/

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long N, M, total = 0;

    cin >> N >> M;

    for(int i = 0; i < N + M; i ++){
        long long k;

        cin >> k;

        total += k;
    }

    cout << total;
    return 0;
}
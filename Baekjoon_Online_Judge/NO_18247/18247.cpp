#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 14                   | 
 | 18247 겨울왕국 티켓 예매    | 
 ---------------------------- 
*/

int main(){
    int T;

    cin >> T;

    for(int i = 0; i < T; i ++){
        int N, M;

        cin >> N >> M;

        if(N < 12 or M < 4) cout << -1 << endl;
        else cout << 11 * M + 4 << endl;
    }
    
    return 0;
}

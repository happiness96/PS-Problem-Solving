#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 파티셰리                   | 
 ---------------------------- 
*/

int main(){
    int T;

    cin >> T;
    
    for(int testcase = 1; testcase <= T; testcase ++){
        int N, flag = 0;

        cin >> N;

        for(int i = 0; i < N / 11 + 1; i ++){
            for(int j = 0; j < N / 9 + 1; j ++){
                for(int k = 0; k < N / 7 + 1; k ++){
                    if(i * 11 + j * 9 + k * 7 == N){
                        flag = 1;
                        break;
                    }
                }

                if(flag) break;
            }

            if(flag) break;
        }

        cout << "Case #" << testcase << endl;
        if(flag) cout << "YES" << endl;
        else cout << "NO" << endl;
    }

    return 0;
}

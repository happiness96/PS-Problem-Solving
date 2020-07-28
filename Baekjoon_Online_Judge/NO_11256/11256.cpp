#include <iostream>
#include <algorithm>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 11256 사탕                | 
 ---------------------------- 
*/

int main(){
    int T;
    
    cin >> T;

    for(int t = 0; t < T; t ++){
        int J, N;

        cin >> J >> N;
        
        int box[N];

        for(int i = 0; i < N; i ++){
            int R, C;

            cin >> R >> C;
            box[i] = R * C;
        }

        sort(box, box + N);

        for(int i = N - 1; i >= 0; i --){
            J -= box[i];
            
            if(J <= 0){
                cout << N - i << endl;
                break;
            }
        }

    }

    return 0;
}

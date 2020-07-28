#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 배드민턴                  | 
 ---------------------------- 
*/

int main(){
    int T;

    cin >> T;

    for(int testcase = 1; testcase <= T; testcase ++){
        int a_score = 0, b_score = 0, win = 0;
        string result;

        cin >> result;

        cout << "Case #" << testcase << endl;

        for(int i = 0; i < result.length(); i ++){
            if(result[i] == 'A'){
                a_score ++;

                if(a_score == 21){
                    win = 1;
                    break;
                }
            }
            
            else {
                b_score ++;

                if(b_score == 21){
                    win = 2;
                    break;
                }
            }
        }
        
        if(win == 0) cout << "Playing" << endl;
        else if(win == 1) cout << "Alice" << endl;
        else cout << "Bob" << endl;
    }
    return 0;
}

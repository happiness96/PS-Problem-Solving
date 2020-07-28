#include <iostream>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 약수의 합                  | 
 ---------------------------- 
*/

int main(){
    int T;
    
    cin >> T;

    for(int testcase = 1; testcase <= T; testcase ++){
        int A, B, total = 0;

        cin >> A >> B;

        for(int num = A; num <= B; num ++){
            for(int div = 1; div <= num; div ++){
                if(num % div == 0)total += div;
            }
        }
        cout << "Case #" << testcase << endl;
        cout << total << endl;
    }
    return 0;
}

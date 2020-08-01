#include <iostream>
#include <algorithm>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 08                 | 
 | Day 02                   | 
 | 2693 N번째 큰 수           | 
 ---------------------------- 
*/

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T;

    cin >> T;

    for(int i = 0; i < T; i ++){
        int A[10];

        for(int i = 0; i < 10; i ++){
            int num;
            cin >> num;

            A[i] = num;
        }

        sort(A, A + 10);

        cout << A[7] << "\n";
    }
    return 0;
}

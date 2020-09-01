#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2020                          | 
 | Month 09                           | 
 | Day 01                             | 
 | 세 수                              | 
 -------------------------------------- 
*/

int main(){
    int A, B, C;

    cin >> A >> B >> C;

    if (A > B){
        int tmp = A;
        A = B;
        B = tmp;
    }

    if (B > C){
        int tmp = B;
        B = C;
        C = tmp;
    }

    if (A > B){
        int tmp = A;
        A = B;
        B = tmp;
    }

    cout << B;

    return 0;
}
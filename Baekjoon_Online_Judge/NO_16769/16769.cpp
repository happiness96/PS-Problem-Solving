#include <iostream>
#include <cmath>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 07                 | 
 | Day 28                   | 
 | 16769 Mixing Milk        | 
 ---------------------------- 
*/

int main(){
    int c1, m1, c2, m2, c3, m3, pour;

    cin >> c1 >> m1 >> c2 >> m2 >> c3 >> m3;

    for(int i = 0; i < 100; i ++){
        if(i % 3 == 0){
            pour = min(m1, c2 - m2);

            m2 += pour;
            m1 -= pour;
        }

        else if(i % 3 == 1){
            pour = min(m2, c3 - m3);

            m3 += pour;
            m2 -= pour;
        }

        else{
            pour = min(m3, c1 - m1);

            m1 += pour;
            m3 -= pour;
        }
    }

    cout << m1 << endl << m2 << endl << m3;

    return 0;
}
